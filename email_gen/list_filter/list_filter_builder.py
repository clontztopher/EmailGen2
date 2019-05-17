import django_filters
from django_filters.widgets import CSVWidget
from django.db.models import Q
from ..constants import LICENSE_TYPES, LICENSE_STATUS, TREC_COUNTY_CODES, TREC_COUNTY_CODES_BY_REGION


# Custom Queryset Builder Methods

# Build an xor query set to include domains
def filter_emails_in(queryset, name, domains):
    query = Q(email__icontains=domains[0])
    for domain in domains[1:]:
        query |= Q(email__icontains=domain)
    queryset = queryset.filter(query)
    return queryset


def filter_emails_out(queryset, name, domains):
    for domain in domains:
        queryset = queryset.exclude(email__icontains=domain)
    return queryset


def filter_trec_region(queryset, name, regions):
    county_codes = [code for region_name, region_codes in TREC_COUNTY_CODES_BY_REGION.items()
                    for code in region_codes if region_name in regions]
    queryset = queryset.filter(trec_county__in=county_codes)
    return queryset


# Custom Field Filters
field_filters = {
    'lic_type': [
        django_filters.MultipleChoiceFilter(
            label='License Type',
            field_name='lic_type',
            choices=LICENSE_TYPES
        )
    ],
    'lic_status': [
        django_filters.MultipleChoiceFilter(
            label='License Status',
            field_name='lic_status',
            choices=LICENSE_STATUS
        )
    ],
    'email': [
        django_filters.BaseCSVFilter(
            label='Include Domains',
            field_name='email',
            widget=django_filters.widgets.CSVWidget,
            method=filter_emails_in
        ),
        django_filters.BaseCSVFilter(
            label='Exclude Domains',
            field_name='email',
            widget=django_filters.widgets.CSVWidget,
            method=filter_emails_out
        )
    ],
    'trec_county': [
        django_filters.MultipleChoiceFilter(
            field_name='trec_county',
            choices=[(code, name) for code, name in TREC_COUNTY_CODES.items()],
            label='TREC County'
        ),
        django_filters.MultipleChoiceFilter(
            field_name='trec_county',
            choices=[(name, name) for name, codes in TREC_COUNTY_CODES_BY_REGION.items()],
            method=filter_trec_region,
            label='TREC Region'
        )
    ],
    'trec_ed_status': [
        django_filters.MultipleChoiceFilter(
            label='SAE Status',
            field_name='trec_ed_status',
            choices=[
                ('0', 'No SAE Requirement'),
                ('1', 'SAE Requirement Outstanding'),
                ('2', 'SAE Requirement Met')
            ]
        )
    ],
    'trec_mce_status': [
        django_filters.MultipleChoiceFilter(
            label='CE Status',
            field_name='trec_mce_status',
            choices=[
                ('0', 'No CE Requirement'),
                ('1', 'CE Requirement Outstanding'),
                ('2', 'CE Requirement Met')
            ]
        )
    ],
    'designated_supervisor': [
        django_filters.ChoiceFilter(
            label='Designated Supervisor',
            field_name='designated_supervisor',
            choices=[(0, 'False'), (1, 'True')]
        )
    ]
}


def build_filter(fields):
    """
    Loop over the given fields and see if there are filters
    for them. If so, add each filter as an individual attribute
    to the list_filters dictionary and provide the dictionary
    to the type function to create a new filter type with each
    filter as a different attribute
    :param fields: field headers for list
    :return: dynamically created subclass of django_filters.FilterSet
    """
    list_filters = {}
    for field in fields:
        fs = field_filters.get(field)
        if fs:
            for i, f in enumerate(fs):
                list_filters[field + '_' + str(i)] = f

    ListFilter = type('F', (django_filters.FilterSet,), list_filters)

    return ListFilter
