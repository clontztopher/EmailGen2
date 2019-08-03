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
        self.source_path = 'sources/'
        # Create a storage client and get the bucket
        storage_client = storage.Client()
        bucket_name = settings.SOURCE_BUCKET
        self.bucket = storage_client.get_bucket(bucket_name)

    def get_or_create_blob(self, storage_id) -> storage.Blob:
        blob_name = self.source_path + storage_id
        blob = self.bucket.get_blob(blob_name)
        if not blob:
            blob = self.bucket.blob(blob_name)
        return blob

    def store_file(self, file_bytes, file_name, storage_id) -> storage.Blob:
        # Get or create blob for storing the file
        blob = self.get_or_create_blob(storage_id)
        # Get file extension for determining how to parse file
        path, ext = os.path.splitext(file_name)

        # Check that the file type is supported
        if ext not in ('.csv', '.txt', '.xls', '.xlsx'):
            raise Exception(
                """
                File type not recognized. Please upload as .csv, .txt, or .xls(x). 
                """
            )

        if ext in ['.xls', '.xlsx']:
            excel_file = io.BytesIO(file_bytes)
            df = pd.read_excel(
                excel_file,
                header=None,
                skiprows=[0],
                dtype=str
            )
            upload_string = df.to_csv(
                sep=',',
                header=None,
                index=False,
                index_label=False
            )
            blob.upload_from_string(upload_string)
            return blob

        if ext in ['.csv', '.txt']:
            # Save decoded string of the file
            try:
                file_string = file_bytes.decode('utf8')
            except UnicodeDecodeError:
                file_string = file_bytes.decode('latin')

            # Create file object to be opened by Pandas csv reader
            temp_file = io.StringIO(file_string)
            # Get the delimiter based on extension
            sep = ',' if ext == '.csv' else '\t'
            # Create a dataframe which parses the string
            # and cleans it up avoiding some errors
            df = pd.read_csv(
                filepath_or_buffer=temp_file,
                sep=sep,
                header=None,
                index_col=False,
                dtype=str
            )
            # Convert the data frame to a comma-separated string and upload
            upload_string = df.to_csv(
                sep=',',
                header=False,
                index=False,
                index_label=False
            )
            blob.upload_from_string(upload_string)

            return blob

    def stream_reader(self, storage_id) -> pd.DataFrame:
        blob = self.get_or_create_blob(storage_id)
        blob_string = blob.download_as_string()
        blob_stream = io.BytesIO(blob_string)
        return pd.read_csv(
            filepath_or_buffer=blob_stream,
            header=None,
            chunksize=20000,
            encoding='utf8',
            index_col=False,
            dtype=str
        )
