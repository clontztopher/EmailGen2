import re
import io
import pandas as pd
from django.test import TestCase, Client
from .fixtures import get_upload_test
from ..constants import TREC_COUNTY_CODES_BY_REGION


class ViewTests(TestCase):

    def setUp(self) -> None:
        self.instance = get_upload_test('aptx')
        self.client = Client()
        self.download_path = '/download/' + str(self.instance.pk) + '/'

    def mock_post(self, path, params):
        return self.client.post(path, params)

    def test_download_form_view(self):
        response = self.mock_post(self.download_path, {'file_name': 'test'})
        self.assertEqual(
            response.get('Content-Disposition'),
            'attachment; filename=test.csv'
        )
        response_reader = pd.read_csv(io.BytesIO(response.content), usecols=range(6))
        print(response_reader.head())
        print(response_reader.count())
        # data = response.content.decode('utf-8').split('\r\n')
        # for i in range(20):
        #     entity = self.instance.zip_row(data[i].split(','))
        #     self.assertEqual(18, len(entity), msg=data)

    def test_download_form_filters_emails(self):
        response = self.mock_post(self.download_path, {
            'file_name': 'test',
            'email_domains': '@aol',
            'email_domains_inclusive': True
        })
        lines = response.content.decode('utf-8').split('\r\n')
        for i, line in enumerate(lines):
            line_list = line.split(',')
            line_dict = self.instance.zip_row(line_list)
            try:
                email = line_dict['email']
            except Exception as err:
                continue
            if email and ('@' in email):
                self.assertTrue((re.search('aol', email, re.IGNORECASE)), email)

    def test_download_form_filters_exp_date(self):
        response = self.mock_post(self.download_path, {
            'file_name': 'test',
            'exp_date': '2020-02-29'
        })
        lines = response.content.decode('utf-8').split('\r\n')
        for i in range(20):
            if not i == 0:
                entity = self.instance.zip_row(lines[i].split(','))
                self.assertEqual(entity['exp_date'], '02-29-2020')

    def test_download_form_filters_counties(self):
        response = self.mock_post(self.download_path, {
            'file_name': 'test',
            'counties': ['227']
        })
        lines = response.content.decode('utf-8').split('\r\n')
        for i in range(20):
            if not i == 0:
                entity = self.instance.zip_row(lines[i].split(','))
                self.assertEqual(entity['mail_county'], '227')

    def test_download_form_filters_regions(self):
        response = self.mock_post(self.download_path, {
            'file_name': 'test',
            'counties': [],
            'regions': ['Austin']
        })
        lines = response.content.decode('utf-8').split('\r\n')
        for i in range(20):
            if not i == 0:
                entity = self.instance.zip_row(lines[i].split(','))
                self.assertTrue(entity['mail_county'] in TREC_COUNTY_CODES_BY_REGION['Austin'])

    def test_download_form_filters_date_range(self):
        response = self.mock_post(self.download_path, {
            'file_name': 'test',
            'exp_date_range_min': '2019-04-30',
            'exp_date_range_max': '2019-05-31'
        })
        lines = response.content.decode('utf-8').split('\r\n')
        for i in range(20):
            if not i == 0:
                entity = self.instance.zip_row(lines[i].split(','))
                print(entity)
