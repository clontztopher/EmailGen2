import csv
from django.http import HttpResponse
from django.shortcuts import render
from ..models import SourceListModel
from ..list_filter.list_filter import PersonFilter


def download_form(request, file_name):
    source_instance = SourceListModel.objects.get(file_name=file_name)
    results_available = bool(request.GET)
    f = PersonFilter(request.GET, queryset=source_instance.people.all())

    # if results_available:
    #     response = HttpResponse(content_type='text/csv')
    #     fname = source_instance.display_name
    #     fname.replace(' ', '')
    #     fname = fname + '.csv'
    #     response['Content-Disposition'] = 'attachment; filename="%s"' % fname

    return render(request, 'email_gen/list-filter.html', {
        'filter': f,
        'source_instance': source_instance,
        'results_available': results_available
    })
