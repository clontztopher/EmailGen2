import os
from django.db import models
from django.dispatch import receiver

from .aptx_model_config import AppTxConfig
from .retx_model_config import ReTxConfig


def upload_path(instance, name):
    """
    Dynamically find the correct file path and
    delete previous file if there is one.
    """
    ext = name.split('.')[-1]
    file_name = instance.list_type + '.' + ext
    target_path = os.path.join('email_gen', 'uploads', file_name)
    if os.path.isfile(target_path):
        os.remove(target_path)
    return target_path


class SourceListFileModel(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=upload_path)
    list_type = models.CharField(max_length=4, default='retx', editable=False)
    display_name = models.CharField(max_length=30, default='Real Estate - TX', editable=False)

    @classmethod
    def save_file(cls, list_type, file):
        """ Update or create model based on filename """
        if not list_type or not file:
            raise Exception(
                'UploadFileModel.save_file called with incorrect arguments')

        try:
            instance = cls.objects.get(list_type=list_type)
            instance.file = file
        except:
            instance = None

        if not instance:
            if list_type == 'aptx':
                instance = cls(file=file, list_type=list_type, display_name=AppTxConfig.FILE_NAME)
                instance.config = AppTxConfig
            if list_type == 'retx':
                instance = cls(file=file, list_type=list_type, display_name=ReTxConfig.FILE_NAME)
                instance.config = ReTxConfig

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
        instance.file_exists = cls.file_exists_for(instance)

        return instance

    @classmethod
    def file_exists_for(cls, instance):
        return os.path.isfile(instance.file.path)

    def __str__(self):
        date = self.update_date if self.update_date else self.upload_date
        return self.display_name + ", Updated - " + date.strftime('%c')


@receiver(models.signals.post_delete, sender=SourceListFileModel)
def delete_file_on_model_delete(sender, instance, **kwargs):
    """ Delete file if model is deleted """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
