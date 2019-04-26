import re


def in_list_insensitive(opts):
    """ Default parser: Filters value based on list of possible values """
    filter_items = opts['main']

    def in_list_insensitive_predicate(val):
        filtered = [x for x in filter_items if re.search(x, val)]
        return bool(filtered)

    return in_list_insensitive_predicate


def email_domains(opts):
    domains_str = opts['main']
    domains = list(map(str.strip, domains_str.split(',')))

    def email_domains_predicate(email):
        for domain in domains:
            if domain in email:
                return True
        return False

    return email_domains_predicate


# def lic_status_trec(opts):
#     def lic_status_trec_predicate(lic_status):
#         status = opts['lic_status']['main'] or 40
#         return int(lic_status) <= status
#
#     return lic_status_trec_predicate


def make_parser(field: str, parser_name: str, parser_opts: dict) -> callable:
    validator = get_parser(parser_name)
    loaded_validator = validator(parser_opts)
    inclusive = True
    if 'inclusive' in parser_opts:
        inclusive = parser_opts['main']

    def validate(entity):
        return loaded_validator(entity[field]) and inclusive

    return validate


main = in_list_insensitive


def get_parser(name):
    return globals()[name]
