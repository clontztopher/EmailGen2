class AppTxConfig:
    HEADERS = ['lic_type', 'lic_num', 'full_name', 'suffix', 'lic_status', 'lic_date', 'exp_date',
               'email', 'phone', 'mail_1', 'mail_2', 'mail_3', 'mail_city', 'mail_state', 'mail_zip',
               'mail_county', 'agency_id', 'supervises_trainees']

    FILE_NAME = 'Appraisal - TX'

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
            index_col=1
        )
