import django_filters
from email_gen.list_filter.list_filter_methods import dates_match, filter_trec_region, filter_emails_in, \
    filter_emails_out


class FilterFormREIApp(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(FilterFormREIApp, self).__init__(*args, **kwargs)
        self.form.fields['lic_type'].widget.attrs['class'] = 'form-control'
        self.form.fields['application_date_range'].widget.widgets[0].attrs['class'] = 'datepicker form-control'
        self.form.fields['application_date_range'].widget.widgets[1].attrs['class'] = 'datepicker form-control'

    lic_type = django_filters.MultipleChoiceFilter(
        field_name='lic_type',
        choices=[('BRK', 'Broker'), ('SALE', 'Sales Agent')]
    )

    application_date_range = django_filters.DateFromToRangeFilter(
        field_name='app_date_orig'
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
