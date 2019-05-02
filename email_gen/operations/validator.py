import re
import datetime
import pandas as pd


def make_search(checklist):
    def list_search(val):
        if not isinstance(val, str):
            return False
        return any([re.search(item, val, re.IGNORECASE) for item in checklist])

    return list_search


def make_range_check(low=None, high=None):
    if low and high:
        return lambda val: low <= val.date() <= high
    elif low:
        return lambda val: val.date() >= low
    else:
        return lambda val: val.date() <= high


def make_negated_check(predicate):
    def negated_check(*args, **kwargs):
        return not predicate(*args, **kwargs)

    return negated_check


def make_date_list_check(dates):
    def date_list_check(date):
        return any([date == d for d in dates])

    return date_list_check


def get_trec_fltrs(post_data):
    fltrs = {}

    if post_data.get('exp_dates'):
        exp_dates = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in post_data['exp_dates']]
        fltrs['exp_date'] = lambda val: any([val.date() == d for d in exp_dates])
    else:
        if post_data.get('exp_date_range_min') \
                or post_data.get('exp_date_range_max'):
            fltrs['exp_date'] = make_range_check(low=post_data['exp_date_range_min'],
                                                 high=post_data['exp_date_range_max'])

    if post_data.get('email_domains'):
        inclusive = post_data['email_domains_inclusive']
        search = make_search(post_data['email_domains'])
        fltrs['email'] = search if inclusive else make_negated_check(search)

    if post_data.get('lic_type'):
        fltrs['lic_type'] = post_data['lic_type']

    if post_data.get('lic_status'):
        fltrs['lic_status'] = post_data['lic_status']

    if post_data.get('county_codes'):
        fltrs['mail_county'] = post_data['county_codes']

    return fltrs


def get_retx_fltrs(post_data):
    fltrs = get_trec_fltrs(post_data)

    if post_data.get('sae_status', False):
        fltrs['ed_status'] = post_data['sae_status']

    if post_data.get('ce_status', False):
        fltrs['mce_status'] = post_data['ce_status']

    return fltrs


def make_processor(lst_type, post_data) -> callable:
    fltrs_map = {
        'retx': get_retx_fltrs,
        'aptx': get_trec_fltrs
    }

    fltrs = fltrs_map[lst_type](post_data)

    def process_chunk(chunk: pd.DataFrame) -> pd.DataFrame:
        filtered = []
        for row in chunk.itertuples():
            keep = True
            for name, fltr in fltrs.items():
                val = getattr(row, name)
                if callable(fltr) and not fltr(val):
                    keep = False
                    break
                if isinstance(fltr, list) and val not in fltr:
                    keep = False
                    break
            if keep:
                filtered.append(row)

        return pd.DataFrame(filtered)

    return process_chunk
