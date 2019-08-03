import pandas as pd
from django.db.models import Q
from email_gen.constants import TREC_COUNTY_CODES_BY_REGION


# -----------------------
# Custom Filter Methods
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
