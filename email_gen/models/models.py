from django.db import models


class SourceListModel(models.Model):
    file_name = models.CharField(max_length=60)
    display_name = models.CharField(max_length=60, default='Uploaded List')
    update_date = models.DateField(auto_now=True)
    field_labels = models.TextField(blank=True)
    field_types = models.TextField(blank=True)

    def __str__(self):
        return '%s - %s' % (self.file_name, self.update_date)


class Person(models.Model):
    # Uses custom id so it can be attached to foreign fields before
    # bulk creating the instances. MySQL doesn't like the Django UUID field
    # so create it as a BigInt for now. Maybe update if moved to Postgres.
    id = models.BigIntegerField(primary_key=True, editable=False)
    fullname = models.CharField(max_length=180, blank=True)
    firstname = models.CharField(max_length=60, blank=True)
    middlename = models.CharField(max_length=60, blank=True)
    lastname = models.CharField(max_length=60, blank=True)
    suffix = models.CharField(max_length=10, blank=True)
    source_list = models.ForeignKey(SourceListModel, on_delete=models.CASCADE, related_name='people')


class EmailAttribute(models.Model):
    field_label = models.CharField(max_length=32, default='email')
    email = models.EmailField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class DateAttribute(models.Model):
    field_label = models.CharField(max_length=32, default='date_field')
    date = models.DateField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class NumericAttribute(models.Model):
    field_label = models.CharField(max_length=32, default='numeric_field')
    num = models.IntegerField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class TextAttribute(models.Model):
    field_label = models.CharField(max_length=32, default='text_field')
    text = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

# class TrecLicenseStatus(models.Model):
#     DEFAULT_NAME = 'lic_status'
#     STATUSES = [
#         ('20', 'Current and Active'),
#         ('21', 'Current and Inactive'),
#         ('30', 'Probation and Active'),
#         ('31', 'Probation and Inactive'),
#         ('45', 'Expired'),
#         ('47', 'Suspended'),
#         ('56', 'Relinquished'),
#         ('57', 'Revoked'),
#         ('80', 'Deceased')
#     ]
#
#     status = models.CharField(choices=STATUSES, max_length=25)
#     person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='license_status')

# class LicenseNumber(models.Model):
#     DEFAULT_NAME = 'lic_num'
#     license = models.IntegerField()
#     person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='license_number')
#
#
# class TrecLicenseType(models.Model):
#     DEFAULT_NAME = 'lic_type'
#     LICENSE_TYPES = [
#         ('SALE', 'Sales Agent'),
#         ('BRK', 'Individual Broker'),
#         ('BLLC', 'Limited Liability Corporation Broker'),
#         ('BCRP', 'Corporation Broker'),
#         ('6', 'Partnership Broker'),
#         ('REB', 'Broker Organization Branch'),
#         ('PRIN', 'Professional Inspector'),
#         ('REIN', 'Real Estate Inspector'),
#         ('APIN', 'Apprentice Inspector'),
#         ('ILLC', 'Professional Inspector, LLC'),
#         ('ICRP', 'Professional Inspector, Corporation'),
#         ('ERWI', 'Easement and Right-of-Way, Individual'),
#         ('ERWO', 'Easement and Right-of-Way, Business')
#     ]
#
#     lic_type = models.CharField(choices=LICENSE_TYPES, max_length=50)
#     person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='license_type')
