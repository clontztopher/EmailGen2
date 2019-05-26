import json
import pandas as pd
from django.test import TestCase, Client
from ..models import SourceListModel
from .file_storage import FileStorageService


class FileStorageTests(TestCase):
    # Use same client and source instance across all tests
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.source_instance = SourceListModel.objects.create(
            file_id='intx',
            display_name='Appraiser - TX',
            source_url='https://www.trec.texas.gov/sites/default/files/high-value-data-sets/inspfile.zip',
            zip_file_name='inspfile.txt'
        )

    # Use new storage service for each test
    def setUp(self) -> None:
        self.storage_service = FileStorageService()

    def test_storage_service_save_file(self):
        # Get version of current file
        initial_version = self.storage_service.get_blob('intx').generation
        # Save file
        self.storage_service.save_file('intx')
        # Get new version
        new_version = self.storage_service.get_blob('intx').generation

        self.assertNotEqual(initial_version, new_version)

    def test_storage_service_get_reader(self):
        reader = self.storage_service.get_file_reader('intx')
        self.assertTrue(type(next(reader)) == pd.DataFrame)

    def test_file_fetch_api_success(self):
        res = self.client.get('/save-source/intx/')
        self.assertEqual(json.loads(res.content), {'message': 'success'})

    def test_file_fetch_api_fail(self):
        res = self.client.get('/save-source/test/')
        self.assertEqual(json.loads(res.content), {'message': "No source data for list id 'test'"})
