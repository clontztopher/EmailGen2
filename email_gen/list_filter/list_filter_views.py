import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from email_gen.models import SourceListModel
from email_gen.sources_conf import get_resources_for


@login_required
def download_form(request, file_id):
    source_instance = SourceListModel.objects.get(file_id=file_id)
    fields = source_instance.get_meta()

    # Collect needed data and classes
    licensee_model, form_template, form_class = get_resources_for(file_id).values()

    # Create django-filter form from form class
    f = form_class(request.GET, queryset=licensee_model.objects.all())

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

    return render(request, 'email_gen/%s.html' % form_template, {
        'form': f.form,
        'source_instance': source_instance
    })
