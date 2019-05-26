import io, zipfile
import pandas as pd
import requests
from google.cloud import storage
from django.conf import settings
from ..models import SourceListModel


class FileStorageService:
    """
    Works with Google Cloud Storage to retrieve and save source files
    """

    def __init__(self):
        # Create a storage client and get the bucket
        # specified in settings
        storage_client = storage.Client()
        bucket_name = settings.SOURCE_LIST_STORAGE_BUCKET_NAME
        self.bucket = storage_client.get_bucket(bucket_name)
        # Set path for saving
        self.source_path = settings.SOURCES_PATH

    def get_file_path(self, file_id):
        return self.source_path + file_id

    def get_blob(self, file_id):
        return self.bucket.get_blob(self.get_file_path(file_id))

    def get_file_reader(self, file_id, chunksize=5000):
        # Get file blob
        blob = self.get_blob(file_id)

        # Save the byte string in a variable and create a read stream
        blob_string = blob.download_as_string()
        file = io.BytesIO(blob_string)

        # Create a file stream reader
        reader = pd.read_csv(
            filepath_or_buffer=file,
            sep='\t',
            encoding='latin',
            header=None,
            chunksize=chunksize,
            dtype=str
        )
        return reader

    def save_file(self, file_id):
        """
        Save file from zip archive at URL location
        :param file_id:
        :return: None
        """
        source_instance = SourceListModel.objects.get(file_id=file_id)
        # URL of zip file
        source_url = source_instance.source_url
        # Name of file in zip archive
        zip_file_name = source_instance.zip_file_name
        # Make request to zip file location
        r = requests.get(source_url, headers={'User-Agent': 'Mozilla/5.0'})
        # Send bytes from response content to zip file
        zip_file = zipfile.ZipFile(io.BytesIO(r.content))

        # Access member
        with zip_file.open(zip_file_name) as txt_file:
            blob = self.get_blob(file_id)
            blob.upload_from_file(txt_file)

# def get_list_sample(file_id):
#     # Grab the storage bucket
#     bucket = get_source_bucket()
#
#     # Build path to source files in bucket
#     file_path = get_file_path(file_id)
#
#     # Get file blob
#     blob = bucket.get_blob(file_path)
#
#     # Save the byte string in a variable and create a read stream
#     blob_string = blob.download_as_string()
#     file = io.BytesIO(blob_string)
#
#     # Create a file stream reader
#     reader = pd.read_csv(
#         filepath_or_buffer=file,
#         sep='\t',
#         encoding='latin',
#         header=None,
#         dtype=str
#     )
#     head = reader.head().fillna('')
#     return [content.tolist() for label, content in head.iteritems()]
