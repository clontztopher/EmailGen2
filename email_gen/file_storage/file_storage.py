import io, os
import pandas as pd
from google.cloud import storage
from django.conf import settings


class FileStorageService:
    """
    Works with Google Cloud Storage to store and retrieve source files
    """

    def __init__(self):
        # Set path for saving/retrieving file
        self.source_path = settings.SOURCES_PATH
        # Create a storage client and get the bucket
        storage_client = storage.Client()
        bucket_name = settings.SOURCE_LIST_STORAGE_BUCKET_NAME
        self.bucket = storage_client.get_bucket(bucket_name)

    def get_or_create_blob(self, file_name) -> storage.Blob:
        blob_name = self.source_path + file_name
        blob = self.bucket.get_blob(blob_name)
        if not blob:
            blob = self.bucket.blob(blob_name)
        return blob

    def store_file(self, file, file_name) -> storage.Blob:
        path, ext = os.path.splitext(file_name)
        name = path.split('/')[-1]

        # Get or create blob for storing the file
        blob = self.get_or_create_blob(name)

        if ext not in ('.csv', '.txt'):
            raise Exception(
                """
                File type not recognized. Please upload as .csv, .txt. A .zip 
                archive may also be uploaded as long as the list is the first 
                file in the archive.
                """
            )

        reader_opts = dict(
            filepath_or_buffer=file,
            header=None,
            dtype=str,
            sep=',' if ext == '.csv' else '\t'
        )

        try:
            df = pd.read_csv(**reader_opts)
        except:
            try:
                df = pd.read_csv(**reader_opts, encoding='latin')
            except:
                raise Exception('Unrecognized character encoding.')

        csv_str = df.to_csv()
        csv_file = io.StringIO(csv_str)
        blob.upload_from_file(csv_file)

        return blob

    def stream_reader(self, file_name):
        blob = self.get_or_create_blob(file_name)
        blob_string = blob.download_as_string()
        blob_stream = io.BytesIO(blob_string)
        return pd.read_csv(
            filepath_or_buffer=blob_stream,
            header=None,
            chunksize=20000
        )

    # def get_stream_from_bucket(self):
    #     blob = self.get_blob()
    #     blob_string = blob.download_as_string()
    #     return io.BytesIO(blob_string)

    # def get_reader(self, **read_opts):
    #     # Merge default options and read_opts before sending in as kwargs
    #     return pd.read_csv(**{**self.DEFAULT_READER_OPTS, **read_opts})
    #
    # def get_reader_from_stream(self):
    #     return self.get_reader(
    #         filepath_or_buffer=self.get_stream_from_bucket(),
    #         encoding=self.source_instance.encoding
    #     )
