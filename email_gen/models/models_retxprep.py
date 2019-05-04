from django.db import models


class RealEstateTexasPrepListModel(models.Model):
    FILE_HEADERS = ['app_id', 'lic_type', 'app_received', 'exp_date', 'last_name', 'first_name', 'middle_name',
                    'suffix', 'street_num', 'mail_1', 'mail_2', 'mail_3', 'mail_city', 'mail_state', 'mail_zip',
                    'phone', 'email',
                    'completed_prelicense', 'completed_sae', 'completed_broker']

    list_type = models.CharField(max_length=100, default='retxprep', editable=False)
    display_name = models.CharField(max_length=100, default='Real Estate License Applications - Texas', editable=False)
    update_date = models.DateTimeField()

    @classmethod
    def get_reader_opts(cls):
        return dict(
            sep='\t',
            header=None,
            names=cls.FILE_HEADERS,
            dtype={header: str for header in cls.FILE_HEADERS},
            chunksize=100000,
            encoding='latin',
            parse_dates=[4, 5]
        )

    def __str__(self):
        return "%s - %s" % (self.display_name, self.update_date.strftime('%c'))


class RealEstateTexasPrepModel(models.Model):
    app_id = models.CharField(max_length=16)
    lic_type = models.CharField(max_length=6)
    app_received = models.DateField()
    exp_date = models.DateField()
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    suffix = models.CharField(max_length=20)
    street_num = models.CharField(max_length=60, blank=True, null=True)
    mail_1 = models.CharField(max_length=60, blank=True, null=True)
    mail_2 = models.CharField(max_length=60, blank=True, null=True)
    mail_3 = models.CharField(max_length=60, blank=True, null=True)
    mail_city = models.CharField(max_length=60, blank=True, null=True)
    mail_state = models.CharField(max_length=4, blank=True, null=True)
    mail_zip = models.CharField(max_length=12, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    completed_prelicense = models.CharField(max_length=3)
    completed_sae = models.CharField(max_length=3)
    completed_broker = models.CharField(max_length=3)

    source_list = models.ForeignKey(RealEstateTexasPrepListModel, on_delete=models.CASCADE, related_name='entities')
