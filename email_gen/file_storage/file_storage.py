import io, zipfile, os, typing
import pandas as pd
import requests
from google.cloud import storage
from django.conf import settings


class FileStorageService:
    """
    Works with Google Cloud Storage to store and retrieve source files
    """

    # DEFAULT_READER_OPTS = {
    #     'filepath_or_buffer': None,
    #     'header': None,
    #     'chunksize': 30000,
    #     'dtype': str
    # }

    def __init__(self):
        # Set path for saving/retrieving file
        self.source_path = settings.SOURCES_PATH
        # Create a storage client and get the bucket
        storage_client = storage.Client()
        bucket_name = settings.SOURCE_LIST_STORAGE_BUCKET_NAME
        self.bucket = storage_client.get_bucket(bucket_name)

    def get_or_create_blob(self, file_name) -> storage.Blob:
        blob = self.bucket.get_blob(self.source_path + file_name)
        if not blob:
            blob = self.bucket.blob(self.source_path + file_name)
        return blob

    def store_file(self, file, file_name) -> storage.Blob:
        name, ext = os.path.splitext(file_name)
        name = name.split('/')[-1]

        # Get or create blob for storing the file
        blob = self.get_or_create_blob(file_name)

        if not ext in ('.csv', '.txt', '.zip'):
            raise Exception(
                """
                File type not recognized. Please upload as .csv, .txt. A .zip 
                archive may also be uploaded as long as the list is the first 
                file in the archive.
                """
            )

        if 'zip' == ext:
            with zipfile.ZipFile(file) as zip:
                with zip.open(zip.namelist()[0]) as archive_file:
                    name, ext = os.path.splitext(file.name)
                    file = archive_file

        if ext in ('.csv', '.txt'):
            sep = ',' if ext == '.csv' else '\t'
            try:
                df = pd.read_csv(
                    filepath_or_buffer=file,
                    header=None,
                    dtype=str,
                    sep=sep
                )
            except:
                try:
                    df = pd.read_csv(
                        filepath_or_buffer=file,
                        encoding='latin-1',
                        header=None,
                        dtype=str,
                        sep=sep
                    )
                except:
                    raise Exception('Unrecognized character encoding.')

        csv_str = df.to_csv()
        csv_file = io.StringIO(csv_str)
        blob.upload_from_file(csv_file)

        return blob

    # def fetch_and_save(self):
    #     r = requests.get(
    #         self.source_instance.source_url,
    #         headers={'User-Agent': 'Mozilla/5.0'}
    #     )
    #     self.save_file(r.content)

    # Reader-related

    # def get_stream_from_bucket(self):
    #     blob = self.get_blob()
    #     blob_string = blob.download_as_string()
    #     return io.BytesIO(blob_string)
    #
    # def get_reader(self, **opts):
    #     # Merge default options and opts before sending in as kwargs
    #     return pd.read_csv(**{**self.DEFAULT_READER_OPTS, **opts})
    #
    # def get_reader_from_stream(self):
    #     return self.get_reader(
    #         filepath_or_buffer=self.get_stream_from_bucket(),
    #         encoding=self.source_instance.encoding
    #     )
