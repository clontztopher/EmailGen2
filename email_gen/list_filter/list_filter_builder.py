import django_filters
import pandas as pd
from django_filters.widgets import CSVWidget
from django.db.models import Q
from ..constants import TREC_LIC_STATUS, TREC_LIC_TYPES, TREC_COUNTY_CODES, TREC_COUNTY_CODES_BY_REGION


# Instead of creating a new form class for each list, since
# they consist of mostly the same fields, create the forms
# dynamically based on custom filter functions and filter fields

# -----------------------
# Custom Filter Functions
# -----------------------

def filter_emails_in(queryset, name, domains):
    # Build queryset with xor to filter in emails
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


def dates_match(queryset, name, dates):
    # Match any of the individual dates in the submitted list
    dates = [pd.to_datetime(d) for d in dates]
    # Initialize query set with first date
    query = Q(**{name: dates[0]})
    # Build rest of query with xor
    for date in dates[1:]:
        query |= Q(**{name: date})
    queryset = queryset.filter(query)
    return queryset


# --------------
# Custom Filters
# --------------

field_filters = {
    # Uses multiple choice filter with predefined choices
    'lic_type': [
        django_filters.MultipleChoiceFilter(
            label='License Type',
            field_name='lic_type',
            choices=TREC_LIC_TYPES
        )
    ],
    'lic_status': [
        django_filters.MultipleChoiceFilter(
            label='License Status',
            field_name='lic_status',
            choices=TREC_LIC_STATUS
        )
    ],
    # Use CSVFilter for list input with comma separation
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
    # Use multiple choice filter for counties
    'trec_county': [
        django_filters.MultipleChoiceFilter(
            field_name='trec_county',
            choices=[(code, name) for code, name in TREC_COUNTY_CODES],
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
                (0, 'No SAE Requirement'),
                (1, 'SAE Requirement Outstanding'),
                (2, 'SAE Requirement Met')
            ]
        )
    ],
    'trec_mce_status': [
        django_filters.MultipleChoiceFilter(
            label='CE Status',
            field_name='trec_mce_status',
            choices=[
                (0, 'No CE Requirement'),
                (1, 'CE Requirement Outstanding'),
                (2, 'CE Requirement Met')
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

        if 'date' in field:
            # Date fields need to be built at runtime
            # to ensure unique filter instances for however
            # many fields contain the keyword 'date'.
            # One range filter and one comma separated
            # inclusive filter is added per date field
            range_key = field + '_range_filter'
            range_label = 'Date Range: ' + field
            list_filters[range_key] = django_filters.DateFromToRangeFilter(
                label=range_label,
                field_name=field
            )
            indie_key = field + '_indie_filter'
            indie_label = 'Date List: ' + field
            list_filters[indie_key] = django_filters.BaseCSVFilter(
                label=indie_label,
                field_name=field,
                widget=django_filters.widgets.CSVWidget,
                method=dates_match
            )

        # Use the field key to try to get
        # the filters list and, if it exists
        # loop over the filters creating a unique
        # attribute for each before supplying them
        # to the dynamically created filter
        fs = field_filters.get(field)
        if fs:
            for i, f in enumerate(fs):
                list_filters[field + '_' + str(i)] = f

    # Dynamically create the filter class at runtime for customization
    list_filter = type('F', (django_filters.FilterSet,), list_filters)

    return list_filter
