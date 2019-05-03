import csv
import pandas as pd
from django.test import TestCase
from django.core.files import File
from ..models.appraiser_list import AppraiserTexasListModel
from ..models.appraiser_texas import AppraiserTexas
from ..operations.save_list import save_list
from ..operations.download_list import download_list


class DownloadTests(TestCase):

    def setUp(self) -> None:
        with open('email_gen/tests/test-apprfile.txt', 'rb') as f:
            test_file = File(f)
            self.list_instance = save_list(list_type='aptx', file=test_file)

    def test_download(self):
        with open('email_gen/tests/test-download.csv', 'w', newline='') as test_file:
            query_set = AppraiserTexas.objects.all()
            download_list(query_set, test_file)

        test_result = pd.read_csv('email_gen/tests/test-download.csv')
        print(str(test_result[:10]))
