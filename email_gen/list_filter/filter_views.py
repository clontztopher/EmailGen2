from django.shortcuts import render
from ..models import Person
from .list_filter import PersonFilter


def person_filter(request):
    f = PersonFilter(request.GET, queryset=Person.objects.all())
    return render(request, 'email_gen/list-filter.html', {'filter': f})
