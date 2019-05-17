import io
import pandas as pd
from google.cloud import storage
from django.conf import settings


def get_source_bucket():
    storage_client = storage.Client()
    bucket_name = settings.SOURCE_LIST_STORAGE_BUCKET_NAME
    bucket = storage_client.get_bucket(bucket_name)
    return bucket


def get_list_sample(file_name):
    bucket = get_source_bucket()
    blob = bucket.get_blob(file_name)
    blob_string = blob.download_as_string()
    file = io.BytesIO(blob_string)
    reader = pd.read_csv(
        filepath_or_buffer=file,
        sep='\t',
        encoding='latin',
        header=None,
        dtype=str
    )
    head = reader.head().fillna('')
    return [content.tolist() for label, content in head.iteritems()]


def get_file_reader(file_name, chunksize=5000):
    bucket = get_source_bucket()
    blob = bucket.get_blob(file_name)
    blob_string = blob.download_as_string()
    file = io.BytesIO(blob_string)
    reader = pd.read_csv(
        filepath_or_buffer=file,
        sep='\t',
        encoding='latin',
        header=None,
        chunksize=chunksize,
        dtype=str
    )
    return reader
