import re
import datetime
import pandas as pd
from django.test import TestCase
from ..models.aptx_model_config import AppTxConfig
from ..operations import validator as vd


class ValidatorTests(TestCase):

    def setUp(self) -> None:
        self.list_data_reader = pd.read_csv('email_gen/tests/test-apprfile.txt', **AppTxConfig.get_reader_opts())

    def test_validator(self):
        chunk = next(self.list_data_reader)
        processor = vd.make_processor('aptx', {
            'email_domains': ['@hotmail'],
            'exp_dates': ['2019-06-30'],
            'exp_date_range_min': None,
            'exp_date_range_max': None,
            'email_domains_inclusive': True,
            'lic_status': '20'
        })
        chunk = processor(chunk)[['full_name', 'email', 'exp_date', 'lic_status']].head(50)
        for entity in chunk.itertuples():
            self.assertTrue(re.search('@hotmail', entity.email, re.IGNORECASE))
            self.assertTrue(entity.exp_date == datetime.datetime(2019, 6, 30))
            self.assertTrue(entity.lic_status == '20')

