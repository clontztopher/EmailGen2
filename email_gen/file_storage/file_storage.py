import io, zipfile
import pandas as pd
from google.cloud import storage
from django.conf import settings
from ..models import SourceListModel
from ..utils import fetch_file


class FileStorageService:
    """
    Works with Google Cloud Storage to store and retrieve source files
    """
    DEFAULT_READER_OPTS = {
        'filepath_or_buffer': None,
        'sep': '\t',
        'encoding': 'latin',
        'header': None,
        'chunksize': 30000,
        'dtype': str
    }

    def __init__(self, file_id):
        self.file_id = file_id
        # Set path for saving/retrieving file
        self.source_path = settings.SOURCES_PATH + file_id
        self.source_instance = SourceListModel.objects.get(file_id=file_id)
        # Create a storage client and get the bucket
        # specified in settings
        storage_client = storage.Client()
        bucket_name = settings.SOURCE_LIST_STORAGE_BUCKET_NAME
        self.bucket = storage_client.get_bucket(bucket_name)

    def get_blob(self):
        return self.bucket.get_blob(self.source_path)

    def get_reader(self, **opts):
        # Merge default options and opts before sending in as kwargs
        return pd.read_csv(**{**self.DEFAULT_READER_OPTS, **opts})

    def save_from_zip(self, zip_file):
        unzipped = zipfile.ZipFile(io.BytesIO(zip_file))
        with unzipped.open(self.source_instance.zip_file_name) as raw_file:
            blob = self.get_blob()
            blob.upload_from_file(raw_file)

    def fetch_and_save(self):
        # TODO: Assumes zip file, handle other types as well
        file = fetch_file(self.source_instance.source_url)
        self.save_from_zip(file)

    def get_stream_from_bucket(self):
        blob = self.get_blob()
        blob_string = blob.download_as_string()
        return io.BytesIO(blob_string)

    def get_reader_from_stream(self):
        return self.get_reader(filepath_or_buffer=self.get_stream_from_bucket())
