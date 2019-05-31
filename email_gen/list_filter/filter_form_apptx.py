import django_filters
from email_gen.list_filter.list_filter_methods import dates_match, filter_trec_region, filter_emails_in, \
    filter_emails_out
from email_gen.constants import TALCB_LIC_TYPES, TREC_LIC_STATUS, TREC_ED_STATUS, TREC_MCE_STATUS, \
    TREC_COUNTY_CODES_BY_REGION, \
    TREC_COUNTY_CODES


class FilterFormAPTX(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(FilterFormAPTX, self).__init__(*args, **kwargs)
        self.form.fields['lic_type'].widget.attrs['class'] = 'form-control'
        self.form.fields['lic_status'].widget.attrs['class'] = 'form-control'
        self.form.fields['trec_county'].widget.attrs['class'] = 'form-control'
        self.form.fields['trec_region'].widget.attrs['class'] = 'form-control'
        self.form.fields['exp_date_range'].widget.widgets[0].attrs['class'] = 'datepicker form-control'
        self.form.fields['exp_date_range'].widget.widgets[1].attrs['class'] = 'datepicker form-control'
        self.form.fields['exp_date_indie'].widget.attrs['class'] = 'form-control'

    lic_type = django_filters.MultipleChoiceFilter(
        field_name='lic_type',
        choices=TALCB_LIC_TYPES
    )

    lic_status = django_filters.MultipleChoiceFilter(
        field_name='lic_status',
        choices=TREC_LIC_STATUS
    )

    exp_date_range = django_filters.DateFromToRangeFilter(
        field_name='lic_date_exp'
    )

    exp_date_indie = django_filters.BaseCSVFilter(
        field_name='lic_date_exp',
        widget=django_filters.widgets.CSVWidget,
        method=dates_match
    )

    sae_status = django_filters.MultipleChoiceFilter(
        field_name='trec_ed_status',
        choices=TREC_ED_STATUS
    )

    ce_status = django_filters.MultipleChoiceFilter(
        field_name='trec_mce_status',
        choices=TREC_MCE_STATUS
    )

    trec_county = django_filters.MultipleChoiceFilter(
        field_name='trec_county',
        choices=[(code, name) for code, name in TREC_COUNTY_CODES],
        label='TREC County'
    )

    trec_region = django_filters.MultipleChoiceFilter(
        field_name='trec_county',
        choices=[(name, name) for name, codes in TREC_COUNTY_CODES_BY_REGION.items()],
        method=filter_trec_region,
        label='TREC Region'
    )

    include_domains = django_filters.BaseCSVFilter(
        field_name='email',
        widget=django_filters.widgets.CSVWidget,
        method=filter_emails_in
    )

    exclude_domains = django_filters.BaseCSVFilter(
        field_name='email',
        widget=django_filters.widgets.CSVWidget,
        method=filter_emails_out
    )
