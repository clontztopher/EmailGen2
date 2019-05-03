import pandas as pd
from django.test import TestCase
from django.core.files import File

from ..list_upload.upload_utils import save_list
from ..list_download.download_utils import download_list
from ..models.model_utils import get_models


class DownloadTests(TestCase):

    def setUp(self) -> None:
        with open('email_gen/tests/test-apprfile.txt', 'rb') as f:
            test_file = File(f)
            self.list_instance = save_list(list_type='aptx', file=test_file)

    def test_download(self):
        list_model, entity_model = get_models('aptx')
        with open('email_gen/tests/test-download.csv', 'w', newline='') as test_file:
            query_set = entity_model.objects.all()
            download_list('aptx', query_set, test_file)

        test_result = pd.read_csv('email_gen/tests/test-download.csv')
        print(str(test_result[:10]))
