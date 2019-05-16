import django_filters
from django_filters import widgets
from django.db.models import Q
from ..models import Person
from ..constants import LICENSE_TYPES, LICENSE_STATUS, TREC_COUNTY_CODES, TREC_COUNTY_CODES_BY_REGION


class PersonFilter(django_filters.FilterSet):
    lic_type = django_filters.MultipleChoiceFilter(field_name='lic_type', choices=LICENSE_TYPES)
    lic_status = django_filters.MultipleChoiceFilter(field_name='lic_status', choices=LICENSE_STATUS)
    include_domains = django_filters.BaseCSVFilter(
        label='Include Domains',
        field_name='email',
        widget=widgets.CSVWidget,
        method='filter_emails_in',

    )
    exclude_domains = django_filters.BaseCSVFilter(
        label='Exclude Domains',
        field_name='email',
        widget=widgets.CSVWidget,
        method='filter_emails_out'
    )
    trec_county = django_filters.MultipleChoiceFilter(
        field_name='trec_county',
        choices=[(code, name) for code, name in TREC_COUNTY_CODES.items()]
    )
    trec_region = django_filters.MultipleChoiceFilter(
        field_name='trec_county',
        choices=[(name, name) for name, codes in TREC_COUNTY_CODES_BY_REGION.items()],
        method='filter_trec_region'
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

    def filter_trec_region(self, queryset, name, regions):
        county_codes = [code for region_name, region_codes in TREC_COUNTY_CODES_BY_REGION.items()
                        for code in region_codes if region_name in regions]
        queryset = queryset.filter(trec_county__in=county_codes)
        return queryset

    class Meta:
        model = Person
        fields = {}
