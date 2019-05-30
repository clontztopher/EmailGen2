import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import SourceListModel, temp_get_from_id, RealEstateSalesAgentTexas
from .list_filter_builder import build_filter
from .filter_form_trec import FilterFormTREC


@login_required
def download_form(request, file_id):
    source_instance = SourceListModel.objects.get(file_id=file_id)
    fields = source_instance.get_meta()
    # Check to see if query params are present
    # since we don't want to download a CSV
    # of the whole list on initial page visit
    has_query = bool(request.GET)

    # Build filter class based on fields and instantiate
    list_filter_class = build_filter(fields)

    # Create filter using an 'all' query set
    licensee_class = temp_get_from_id(file_id)
    f = list_filter_class(request.GET, queryset=licensee_class.objects.all())

    if has_query:
        # Create CSV response with file name from user input
        download_name = request.GET['filename']
        if download_name == '':
            download_name = source_instance.file_id

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="%s.csv"' % download_name

        # Create a dict writer instance using list fields
        # as header and response as the write target
        writer = csv.DictWriter(response, fields, extrasaction='ignore')
        writer.writeheader()

        # Loop over the query set values and write each row
        # filtering out unused fields beforehand
        for person_dict in f.qs.values():
            writer.writerow({name: value for name, value in person_dict.items()})

        return response

    return render(request, 'email_gen/list-filter.html', {
        'filter': f,
        'source_instance': source_instance
    })


@login_required
def filter_trec(request):
    source_instance = SourceListModel.objects.get(file_id='trec')
    f = FilterFormTREC(request.GET, queryset=RealEstateSalesAgentTexas.objects.all())
    fields = source_instance.get_meta()

    if bool(request.GET):
        # Create CSV response with file name from user input
        download_name = request.GET['filename']
        if download_name == '':
            download_name = source_instance.file_id

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="%s.csv"' % download_name

        # Create a dict writer instance using list fields
        # as header and response as the write target
        writer = csv.DictWriter(response, fields, extrasaction='ignore')
        writer.writeheader()

        # Loop over the query set values and write each row
        # filtering out unused fields beforehand
        for person_dict in f.qs.values():
            writer.writerow({name: value for name, value in person_dict.items()})

        return response

    return render(request, 'email_gen/list-filter.html', {
        'filter': f,
        'source_instance': source_instance
    })
