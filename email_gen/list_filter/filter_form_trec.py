import django_filters
from ..constants import TREC_LIC_TYPES


class FilterFormTREC(django_filters.FilterSet):
    lic_type = django_filters.MultipleChoiceFilter(
        label='License Type',
        field_name='lic_type',
        choices=TREC_LIC_TYPES
    )
