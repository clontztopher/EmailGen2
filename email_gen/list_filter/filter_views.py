from django.shortcuts import render
from ..models import Person, SourceListModel
from .list_filter import ListFilter


def person_filter(request, list_name):
    source_instance = SourceListModel.objects.get(list_name=list_name)
    f = ListFilter(request.GET, queryset=Person.objects.all())
    return render(request, 'email_gen/list-filter.html', {'filter': f})
