import json, os
from google.cloud import storage
import pandas as pd
from django.conf import settings
from django.test import TestCase, Client
from .file_storage import FileStorageService


class FileStorageTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        storage_client = storage.Client()
        cls.bucket = storage_client.get_bucket(settings.SOURCE_LIST_STORAGE_BUCKET_NAME)

    def test_storage_service_creates_blob(self):
        storage_service = FileStorageService()
        intx = storage_service.get_or_create_blob('test.csv')
        self.assertIsNotNone(intx)
        self.assertTrue(isinstance(intx, storage.Blob))

    def test_storage_service_saves_csv(self):
        storage_service = FileStorageService()
        file_name = 'okce-mock.csv'
        path = os.path.join(settings.MOCK_FILE_LOCATION, file_name)

        with open(path) as file:
            file_blob = storage_service.store_file(file, file_name)
            self.assertIsNotNone(file_blob)
            self.assertTrue(isinstance(file_blob, storage.Blob))

    def test_storage_service_saves_txt(self):
        storage_service = FileStorageService()
        file_name = 'inspfile-mock.txt'
        path = os.path.join(settings.MOCK_FILE_LOCATION, file_name)

        with open(path) as file:
            file_blob = storage_service.store_file(file, file_name)
            self.assertIsNotNone(file_blob)
            self.assertTrue(isinstance(file_blob, storage.Blob))

    def test_storage_service_saves_xlsx(self):
        storage_service = FileStorageService()
        file_name = 'okce-mock.xlsx'
        path = os.path.join(settings.MOCK_FILE_LOCATION, file_name)

        with open(path) as file:
            file_blob = storage_service.store_file(file, file_name)
            self.assertIsNotNone(file_blob)
            self.assertTrue(isinstance(file_blob, storage.Blob))
