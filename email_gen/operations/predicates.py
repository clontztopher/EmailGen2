import re
from datetime import datetime
from ..constants import TREC_COUNTY_CODES_BY_REGION


# Default filter that takes a list of items to check the field value against
def in_list_case_insensitive(opts):
    """ Default: Filters value based on list of possible values """
    filter_items = opts['check_list']
    inclusive = opts.get('inclusive', True)

    def in_list_case_insensitive_predicate(val):
        filtered = [x for x in filter_items if re.search(x, val, re.IGNORECASE)]
        # True if item in list and inclusive is True
        # True if item not in list and inclusive is False (exclusive)
        return bool(filtered) and inclusive

    return in_list_case_insensitive_predicate


def email_domains(opts):
    domains_str = opts['domains']

    domains = list(map(str.strip, domains_str.split(',')))
    inclusive = opts.get('inclusive', True)

    def email_domains_predicate(email):
        for domain in domains:
            if domain and re.search(domain, email, re.IGNORECASE):
                return inclusive
        return not inclusive

    return email_domains_predicate


def individual_date(opts):
    def date_predicate(exp_date_str):
        return exp_date_str == opts['date']

    return date_predicate


def date_range(opts):
    def range_predicate(date_str: str):
        exp_date = datetime.strptime(date_str, opts['format'])
        if opts['limit'] == 'min':
            return opts['date'] <= exp_date
        if opts['limit'] == 'max':
            return opts['date'] >= exp_date

    return range_predicate


def trec_county_filter(opts):
    # Convert list to dictionary for instant lookup.
    # Convert code string to int due to inconsistent
    # formatting in source list files.
    counties = {int(county_code): True for county_code in opts['counties']}

    def trec_county_predicate(county_code):
        return counties.get(int(county_code), False)

    return trec_county_predicate


def trec_region_filter(opts):
    counties = [county_code for region in opts['regions'] for county_code in TREC_COUNTY_CODES_BY_REGION[region]]
    return trec_county_filter({'counties': counties})


def get_filter(*name):
    if len(name) is 0:
        return in_list_case_insensitive
    return globals()[name[0]]
