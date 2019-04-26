import datetime
from django.test import TestCase
# from ..models import SourceListFileModel
from email_gen.forms.download.aptx import ApTxFilterForm


class FormTests(TestCase):

    def test_parser_data_appendid(self):
        form = ApTxFilterForm({'file_name': 'test'})

        with self.subTest(msg='Form failed validation'):
            self.assertTrue(form.is_valid())
        filter_data = form.cleaned_data['file_name']
        self.assertTrue(filter_data == 'test')

    def test_form_date_information(self):
        test_date = datetime.datetime(2019, 4, 30).date()
        form = ApTxFilterForm({
            'file_name': 'test',
            'exp_date': '2019-04-30'
        })

        with self.subTest(msg='Form failed validation'):
            self.assertTrue(form.is_valid())

        filter_data = form.get_data()
        self.assertTrue(filter_data['exp_date']['exp_date_filter']['date'] == test_date)

    def test_form_data_counties(self):
        form = ApTxFilterForm({
            'file_name': 'test',
            'counties': ['227']
        })

        with self.subTest(msg='Form failed validation'):
            self.assertTrue(form.is_valid())

        filter_data = form.get_data()
        self.assertTrue(filter_data['mail_county']['trec_county_filter']['counties'] == ['227'])
