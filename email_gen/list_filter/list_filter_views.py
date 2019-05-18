import csv
from django.http import HttpResponse
from django.shortcuts import render
from ..models import SourceListModel
from ..list_filter.list_filter_builder import build_filter


def download_form(request, file_name):
    source_instance = SourceListModel.objects.get(file_name=file_name)
    fields = source_instance.get_meta()
    has_query = bool(request.GET)

    # Build filter class based on fields and instantiate
    ListFilter = build_filter(fields)
    f = ListFilter(request.GET, queryset=source_instance.people.all())

    if has_query:
        # Create CSV response and prepare file name
        download_name = request.GET['filename']
        if download_name == '':
            download_name = source_instance.display_name.replace(' ', '')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="%s.csv"' % download_name

        # Create a dict writer instance using list fields
        # as header and response as the write target
        writer = csv.DictWriter(response, fields)
        writer.writeheader()

        # Loop over the query set values and write each row
        # filtering out unused fields beforehand
        for person_dict in f.qs.values():
            writer.writerow({name: value for name, value in person_dict.items() if name in fields})

        return response

    return render(request, 'email_gen/list-filter.html', {
        'filter': f,
        'source_instance': source_instance
    })
