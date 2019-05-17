import django_filters
from django_filters import widgets
from django.db.models import Q
from ..constants import LICENSE_TYPES, LICENSE_STATUS


class PersonFilter(django_filters.FilterSet):
    lic_type = django_filters.MultipleChoiceFilter(field_name='lic_type', choices=LICENSE_TYPES)
    lic_status = django_filters.MultipleChoiceFilter(field_name='lic_status', choices=LICENSE_STATUS)
    include_domains = django_filters.BaseCSVFilter(
        label='Include Domains',
        field_name='email',
        widget=widgets.CSVWidget,
        method='filter_emails_in'
    )
    exclude_domains = django_filters.BaseCSVFilter(
        label='Exclude Domains',
        field_name='email',
        widget=widgets.CSVWidget,
        method='filter_emails_out'
    )

    def filter_emails_in(self, queryset, name, domains):
        query = Q(email__icontains=domains[0])
        for domain in domains[1:]:
            query |= Q(email__icontains=domain)
        queryset = queryset.filter(query)
        return queryset

    def filter_emails_out(self, queryset, name, domains):
        for domain in domains:
            queryset = queryset.exclude(email__icontains=domain)
        return queryset
