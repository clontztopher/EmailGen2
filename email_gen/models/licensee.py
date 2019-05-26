import uuid
from django.db import models
from .source_list import SourceListModel


# Licensee Abstract Class
class Licensee(models.Model):
    source_list = models.ForeignKey(SourceListModel, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    # Name Fields
    fullname = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    middlename = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)

    # Contact Fields
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=255)
    address_1 = models.CharField(blank=True, null=True, max_length=255)
    address_2 = models.CharField(blank=True, null=True, max_length=255)
    address_3 = models.CharField(blank=True, null=True, max_length=255)
    address_4 = models.CharField(blank=True, null=True, max_length=255)
    city = models.CharField(blank=True, null=True, max_length=255)
    state = models.CharField(blank=True, null=True, max_length=2)
    zip = models.CharField(blank=True, null=True, max_length=20)
    county = models.CharField(blank=True, null=True, max_length=25)

    class Meta:
        abstract = True
