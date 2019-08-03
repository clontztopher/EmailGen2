import os
from django.test import TestCase, Client
from django.conf import settings
from file_storage.storage_service import FileStorageService
from list_save.save_list import save_source
from email_gen.models import SourceListModel

LIST_MOCK_MAP = {
    'trec': 'trecfile-mock.txt',
    'retx-prep': 'REIApplication-mock.txt',
    'aptx': 'apprfile-mock.txt',
    'intx': 'inspfile-mock.txt',
    'okce': 'okce-mock.xlsx',
    'apaz': 'app-az-mock.xlsx',
    'apva': 'app-va-mock.xlsx',
    'apwa': 'app-wa-mock.xlsx'
}


class ListFilterTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.storage_service = FileStorageService()

    def saveDataFor(self, list_id):
        # Create a file stream reader
        reader = self.storage_service.get_reader(**{
            'filepath_or_buffer': os.path.join(settings.BASE_DIR, 'list_mocks', LIST_MOCK_MAP[list_id]),
        })
        save_list(list_id, reader)
        query = SourceListModel.objects.all()
