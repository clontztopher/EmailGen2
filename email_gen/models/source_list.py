from django.db import models


class SourceListModel(models.Model):
    file_id = models.CharField(max_length=60, unique=True)
    display_name = models.CharField(max_length=60, default='Uploaded List', unique=True)
    update_date = models.DateField(auto_now=True)
    field_labels = models.CharField(null=True, max_length=1000)
    source_url = models.URLField(blank=True, null=True)
    zip_file_name = models.CharField(blank=True, null=True, max_length=60)

    @classmethod
    def get_list_options(cls):
        return [(source.file_id, source.display_name) for source in cls.objects.all()]

    def get_meta(self):
        return self.field_labels.split('::')

    def __str__(self):
        return '%s - %s' % (self.display_name, self.update_date)
