from django.db import models
from .constants import LICENSE_STATUS, LICENSE_TYPES, TREC_ED_STATUS, TREC_MCE_STATUS


class SourceListModel(models.Model):
    file_name = models.CharField(max_length=60)
    display_name = models.CharField(max_length=60, default='Uploaded List')
    update_date = models.DateField(auto_now=True)
    field_labels = models.CharField(blank=True, max_length=1000)

    def get_meta(self):
        return self.field_labels.split('::') if self.field_labels != '' else None

    def __str__(self):
        return '%s - %s' % (self.file_name, self.update_date)


class Person(models.Model):
    source_list = models.ForeignKey(SourceListModel, on_delete=models.CASCADE, related_name='people')

    # Uses custom id so it can be attached to foreign fields before
    # bulk creating the instances. MySQL doesn't like the Django UUID field
    # so create it as a BigInt for now. Maybe update if moved to Postgres.
    id = models.BigIntegerField(primary_key=True, editable=False)

    # Name Info
    fullname = models.CharField(max_length=255, blank=True)
    firstname = models.CharField(max_length=255, blank=True)
    middlename = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    suffix = models.CharField(max_length=255, blank=True)

    # Contact Info
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True, max_length=255)
    address_1 = models.CharField(blank=True, max_length=255)
    address_2 = models.CharField(blank=True, max_length=255)
    address_3 = models.CharField(blank=True, max_length=255)
    address_4 = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    state = models.CharField(blank=True, max_length=2)
    zip = models.CharField(blank=True, max_length=20)
    trec_county = models.CharField(blank=True, max_length=3)
    county = models.CharField(blank=True, max_length=25)

    # License Info
    lic_number = models.CharField(blank=True, max_length=20)  # Not guaranteed to be unique across all lists
    lic_status = models.CharField(default='N/A', choices=LICENSE_STATUS, max_length=255)
    lic_type = models.CharField(default='N/A', choices=LICENSE_TYPES, max_length=255)
    lic_date_orig = models.DateField(null=True)
    lic_date_exp = models.DateField(null=True)
    trec_date_app_received = models.DateField(null=True)
    trec_date_app_expires = models.DateField(null=True)

    # Education Info
    trec_ed_status = models.CharField(blank=True, default='n/a', choices=TREC_ED_STATUS, max_length=255)
    trec_mce_status = models.CharField(blank=True, default='n/a', choices=TREC_MCE_STATUS, max_length=255)
    designated_supervisor = models.BooleanField(default=False)
