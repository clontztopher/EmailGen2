from django.db import models
from ..constants import TREC_MCE_STATUS, TREC_ED_STATUS, TREC_LIC_STATUS, TREC_LIC_TYPES


class RealEstateTexasListModel(models.Model):
    FILE_HEADERS = ['lic_type', 'lic_num', 'full_name', 'suffix', 'lic_status', 'lic_date', 'exp_date',
                    'ed_status', 'mce_status', 'des_supervisor', 'phone', 'email', 'mail_1', 'mail_2', 'mail_3',
                    'mail_city', 'mail_state', 'mail_zip', 'mail_county']

    list_type = models.CharField(max_length=4, default='aptx', editable=False)
    display_name = models.CharField(max_length=30, default='Appraisal - Texas', editable=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    @classmethod
    def get_reader_opts(cls):
        return dict(
            sep='\t',
            header=None,
            names=cls.HEADERS,
            dtype={header: str for header in cls.HEADERS},
            chunksize=100000,
            encoding='latin',
            parse_dates=[5, 6],
            index_col=1,
            usecols=range(19)
        )

    def __str__(self):
        date = self.update_date if self.update_date else self.upload_date
        return self.display_name + ", Updated - " + date.strftime('%c')


class RealEstateAgentTexasModel(models.Model):
    lic_type = models.CharField(max_length=4, choices=TREC_LIC_TYPES)
    lic_num = models.PositiveIntegerField()
    full_name = models.CharField(max_length=40)
    suffix = models.CharField(max_length=10, blank=True)
    lic_status = models.PositiveSmallIntegerField(choices=TREC_LIC_STATUS)
    lic_date = models.DateField()
    exp_date = models.DateField()
    ed_status = models.CharField(max_length=3, choices=TREC_ED_STATUS)
    mce_status = models.CharField(max_length=3, choices=TREC_MCE_STATUS)
    des_supervisor = models.CharField(max_length=3)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    mail_1 = models.CharField(max_length=60, blank=True)
    mail_2 = models.CharField(max_length=60, blank=True)
    mail_3 = models.CharField(max_length=60, blank=True)
    mail_city = models.CharField(max_length=60, blank=True)
    mail_state = models.CharField(max_length=4, blank=True)
    mail_zip = models.CharField(max_length=12, blank=True)
    mail_county = models.CharField(max_length=3, blank=True)

    source_list = models.ForeignKey(RealEstateTexasListModel, on_delete=models.CASCADE, related_name='entities')
