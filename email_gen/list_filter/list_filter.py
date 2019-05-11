import django_filters
from ..models import Person


class PersonFilter(django_filters.FilterSet):
    emails = django_filters.CharFilter(lookup_expr='email__icontains')

    class Meta:
        model = Person
        fields = ['emails']
