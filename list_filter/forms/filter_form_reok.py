import django_filters
from ..list_filter_methods import dates_match, filter_emails_in, filter_emails_out


class FilterFormREOK(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(FilterFormREOK, self).__init__(*args, **kwargs)
        self.form.fields['lic_type'].widget.attrs['class'] = 'form-control'
        self.form.fields['lic_status'].widget.attrs['class'] = 'form-control'
        self.form.fields['exp_date_range'].widget.widgets[0].attrs['class'] = 'datepicker form-control'
        self.form.fields['exp_date_range'].widget.widgets[1].attrs['class'] = 'datepicker form-control'
        self.form.fields['exp_date_indie'].widget.attrs['class'] = 'form-control'

    lic_type = django_filters.MultipleChoiceFilter(
        field_name='lic_type',
        choices=(('BR', 'Broker'), ('SA', 'Sales Agent'))
    )

    lic_status = django_filters.MultipleChoiceFilter(
        field_name='lic_status',
        choices=(("A", "Active"), ("I", "Inactive"))
    )

    exp_date_range = django_filters.DateFromToRangeFilter(
        field_name='lic_date_exp'
    )

    exp_date_indie = django_filters.BaseCSVFilter(
        field_name='lic_date_exp',
        widget=django_filters.widgets.CSVWidget,
        method=dates_match
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
