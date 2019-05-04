from django.db import models
from ..constants import APTX_LIC_STATUS, APTX_LIC_TYPES


class AppraiserTexasListModel(models.Model):
    FILE_HEADERS = ['lic_type', 'lic_num', 'full_name', 'suffix', 'lic_status', 'lic_date', 'exp_date',
                    'email', 'phone', 'mail_1', 'mail_2', 'mail_3', 'mail_city', 'mail_state', 'mail_zip',
                    'mail_county', 'agency_id', 'supervisor_trainee']

    list_type = models.CharField(max_length=4, default='aptx', editable=False)
    display_name = models.CharField(max_length=30, default='Appraisal - Texas', editable=False)
    update_date = models.DateTimeField()

    @classmethod
    def get_reader_opts(cls):
        return dict(
            sep='\t',
            header=None,
            names=cls.FILE_HEADERS,
            dtype={header: str for header in cls.FILE_HEADERS},
            chunksize=10000,
            encoding='latin',
            parse_dates=[5, 6]
        )

    def __str__(self):
        return "%s - %s" % (self.display_name, self.update_date.strftime('%c'))


class AppraiserTexasModel(models.Model):
    lic_type = models.CharField(max_length=4, choices=APTX_LIC_TYPES)
    lic_num = models.PositiveIntegerField()
    full_name = models.CharField(max_length=40)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    lic_status = models.PositiveSmallIntegerField(choices=APTX_LIC_STATUS)
    lic_date = models.DateField()
    exp_date = models.DateField()
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mail_1 = models.CharField(max_length=60, blank=True, null=True)
    mail_2 = models.CharField(max_length=60, blank=True, null=True)
    mail_3 = models.CharField(max_length=60, blank=True, null=True)
    mail_city = models.CharField(max_length=60, blank=True, null=True)
    mail_state = models.CharField(max_length=4, blank=True, null=True)
    mail_zip = models.CharField(max_length=12, blank=True, null=True)
    mail_county = models.CharField(max_length=3, blank=True, null=True)
    agency_id = models.CharField(max_length=15, blank=True, null=True)
    supervisor_trainee = models.CharField(max_length=3)

    source_list = models.ForeignKey(AppraiserTexasListModel, on_delete=models.CASCADE, related_name='entities')
