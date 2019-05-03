import io
import re
import math
import pandas as pd
from django.test import TestCase, Client
from django.core.files import File

from ..download_utils import get_form_for
from ...list_upload.upload_utils import save_list
from ...models.model_utils import get_models
from ...constants import TREC_COUNTY_CODES_BY_REGION


def get_upload_test(list_type):
    with open('email_gen/list_download/download_tests/test-apprfile.txt', 'rb') as f:
        test_file = File(f)
        return save_list(list_type, test_file)


class DownloadTests(TestCase):

    def setUp(self) -> None:
        with open('email_gen/list_download/download_tests/test-apprfile.txt', 'rb') as f:
            test_file = File(f)
            self.list_instance = save_list(list_type='aptx', file=test_file)

    def test_download(self):
        list_model, entity_model = get_models('aptx')
        with open('email_gen/list_download/download_tests/test-download.csv', 'w', newline='') as test_file:
            query_set = entity_model.objects.all()
            query_result = list(query_set.values())
            list_headers = list_model.FILE_HEADERS
            df = pd.DataFrame(query_result, columns=list_headers)
            df.to_csv(path_or_buf=test_file, mode='a')

        test_result = pd.read_csv('email_gen/list_download/download_tests/test-download.csv')
        header = test_result.columns[1:].tolist()
        self.assertEqual(header, list_model.FILE_HEADERS)


class DownloadFormTests(TestCase):

    def setUp(self) -> None:
        self.form = get_form_for('aptx')

    def test_parser_data_appendid(self):
        form = self.form({'file_name': 'test'})

        with self.subTest(msg='Form failed validation'):
            self.assertTrue(form.is_valid())
        filter_data = form.cleaned_data['file_name']
        self.assertTrue(filter_data == 'test')

    def test_form_date_information(self):
        post_data = {
            'file_name': 'test',
            'exp_indie_date_0': '2019-04-30'
        }
        form = self.form(post_data)

        with self.subTest(msg='Form failed validation'):
            self.assertTrue(form.is_valid())

        filter_data = form.get_data(post_data)
        self.assertTrue('2019-04-30' in filter_data['exp_dates'])

    def test_form_data_counties(self):
        form = self.form({
            'file_name': 'test',
            'counties': ['227']
        })

        with self.subTest(msg='Form failed validation'):
            self.assertTrue(form.is_valid())

        filter_data = form.get_data()
        self.assertTrue('227' in filter_data['county_codes'])


class DownloadQueryTests(TestCase):
    def setUp(self) -> None:
        self.instance = get_upload_test('aptx')

    def test_basic_query(self):
        list_model, entity_model = get_models('aptx')
        appraisers = entity_model.objects.filter(lic_type__in=['APCR'])
        for appraiser in appraisers[:10]:
            print(appraiser.__dict__)


class ViewTests(TestCase):

    def setUp(self) -> None:
        self.instance = get_upload_test('aptx')
        self.client = Client()
        self.download_path = '/download/' + str(self.instance.list_type) + '/'

    def mock_post(self, path, params):
        return self.client.post(path, params)

    def test_download_form_view(self):
        response = self.mock_post(self.download_path, {'file_name': 'test'})
        self.assertEqual(
            response.get('Content-Disposition'),
            'attachment; filename=test.csv'
        )
        dataframe = pd.read_csv(io.BytesIO(response.content))
        header = dataframe.columns[1:].tolist()
        self.assertEqual(header, self.instance.FILE_HEADERS)

    def test_download_form_filters_emails_inclusive(self):
        response = self.mock_post(self.download_path, {
            'file_name': 'test',
            'email_domains': '@aol',
            'email_domains_inclusive': True
        })
        dataframe = pd.read_csv(io.BytesIO(response.content))
        for row in dataframe.itertuples():
            self.assertTrue(re.search('@aol', row.email, re.IGNORECASE))

    def test_download_form_filters_emails_exclusive(self):
        response = self.mock_post(self.download_path, {
            'file_name': 'test',
            'email_domains': '@aol',
            'email_domains_inclusive': False
        })
        dataframe = pd.read_csv(io.BytesIO(response.content))
        dataframe = dataframe.fillna('')
        for row in dataframe.itertuples():
            self.assertFalse(re.search('@aol', row.email, re.IGNORECASE), row.email)

    def test_download_form_filters_exp_date(self):
        response = self.mock_post(self.download_path, {
            'file_name': 'test',
            'exp_indie_date': '2020-02-29'
        })
        dataframe = pd.read_csv(io.BytesIO(response.content))
        dataframe = dataframe.fillna('')
        for row in dataframe.itertuples():
            self.assertTrue(row.exp_date == '2020-02-29', row.exp_date)

    def test_download_form_filters_exp_date_range(self):
        response = self.mock_post(self.download_path, {
            'file_name': 'test',
            'exp_date_range_min': '2020-02-29',
            'exp_date_range_max': '2020-04-30'
        })
        dataframe = pd.read_csv(io.BytesIO(response.content))
        dataframe = dataframe.fillna('')
        for row in dataframe.itertuples():
            self.assertTrue(row.exp_date in ('2020-02-29', '2020-03-31', '2020-04-30'), row.exp_date)

    def test_download_form_filters_counties(self):
        response = self.mock_post(self.download_path, {
            'file_name': 'test',
            'counties': ['227']
        })
        dataframe = pd.read_csv(io.BytesIO(response.content))
        dataframe = dataframe.fillna('')
        for row in dataframe.itertuples():
            self.assertTrue(row.mail_county == 227, row.mail_county)

    def test_download_form_filters_regions(self):
        response = self.mock_post(self.download_path, {
            'file_name': 'test',
            'counties': [],
            'regions': ['Austin']
        })
        dataframe = pd.read_csv(io.BytesIO(response.content))
        dataframe = dataframe.fillna('')
        for row in dataframe.itertuples():
            county_in_region = any(
                [row.mail_county == int(county) for county in TREC_COUNTY_CODES_BY_REGION['Austin']]
            )
            self.assertTrue(county_in_region, row.mail_county)
