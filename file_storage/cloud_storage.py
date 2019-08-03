from django.conf import settings
from django.core.files.storage import Storage
from google.cloud import storage


class SourceStorage(Storage):
    def __init__(self):
        client = storage.Client()
        self.bucket = client.get_bucket(settings.SOURCE_BUCKET)
