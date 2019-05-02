from django.db import models
from django.dispatch import receiver
from django.conf import settings
from google.cloud import storage

from .aptx_model_config import AppTxConfig
from .retx_model_config import ReTxConfig


class SourceListFileModel(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    file_name = models.CharField(max_length=40, default='retx')
    list_type = models.CharField(max_length=4, default='retx', editable=False)
    display_name = models.CharField(max_length=30, default='Real Estate - TX', editable=False)

    @classmethod
    def save_file(cls, list_type, file):
        try:
            instance = cls.objects.get(list_type=list_type)
        except:
            instance = None

        if not instance:
            if list_type == 'aptx':
                instance = cls(list_type=list_type, display_name=AppTxConfig.FILE_NAME, file_name=file.name)
                instance.config = AppTxConfig
            if list_type == 'retx':
                instance = cls(list_type=list_type, display_name=ReTxConfig.FILE_NAME, file_name=file.name)
                instance.config = ReTxConfig

        bucket_name = settings.SOURCE_LIST_STORAGE_BUCKET_NAME
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(file.name)
        blob.upload_from_file(file)

        instance.save()

        return instance

    @classmethod
    def get_instance(cls, list_type):
        instance = cls.objects.get(list_type=list_type)
        if list_type == 'aptx':
            config = AppTxConfig
        if list_type == 'retx':
            config = ReTxConfig

        instance.config = config
        instance.file_exists = True

        return instance

    def __str__(self):
        date = self.update_date if self.update_date else self.upload_date
        return self.display_name + ", Updated - " + date.strftime('%c')

# @receiver(models.signals.post_delete, sender=SourceListFileModel)
# def delete_file_on_model_delete(sender, instance, **kwargs):
#     """ Delete file if model is deleted """
#     if instance.file:
#         instance.file.storage.delete(instance.file)
