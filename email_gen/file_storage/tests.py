import os
from google.cloud import storage
from django.conf import settings
from django.test import TestCase
from .file_storage import FileStorageService


class FileStorageTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        storage_client = storage.Client()
        cls.bucket = storage_client.get_bucket(settings.SOURCE_LIST_STORAGE_BUCKET_NAME)

    def test_storage_service_creates_blob(self):
        storage_service = FileStorageService()
        intx = storage_service.get_or_create_blob('test')
        self.assertIsNotNone(intx)
        self.assertTrue(isinstance(intx, storage.Blob))

    def test_storage_service_saves_csv(self):
        storage_service = FileStorageService()
        upload_name = 'inspfile.csv'
        path = os.path.join(settings.MOCK_FILE_LOCATION, upload_name)

        with open(path, 'rb') as file:
            file_bytes = file.read()
            file_blob = storage_service.store_file(file_bytes, upload_name, 'intx')
            self.assertTrue(file_blob.exists())
            self.assertTrue(isinstance(file_blob, storage.Blob))

    def test_storage_service_saves_txt(self):
        storage_service = FileStorageService()
        upload_name = 'apprfile-mock.txt'
        path = os.path.join(settings.MOCK_FILE_LOCATION, upload_name)

        with open(path, 'rb') as file:
            file_bytes = file.read()
            file_blob = storage_service.store_file(file_bytes, upload_name, 'aptx')
            self.assertTrue(file_blob.exists())
            self.assertTrue(isinstance(file_blob, storage.Blob))

    def test_storage_service_saves_xlsx(self):
        storage_service = FileStorageService()
        upload_name = 'okce-mock.xlsx'
        path = os.path.join(settings.MOCK_FILE_LOCATION, upload_name)

        with open(path, 'rb') as file:
            file_bytes = file.read()
            file_blob = storage_service.store_file(file_bytes, upload_name, 'reok')
            self.assertTrue(file_blob.exists())
            self.assertTrue(isinstance(file_blob, storage.Blob))

    def test_gets_reader(self):
        storage_service = FileStorageService()
        stream_reader = storage_service.stream_reader('intx')
        self.assertIsNotNone(stream_reader)
