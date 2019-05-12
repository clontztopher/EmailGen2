from django.shortcuts import render
from ..models import SourceListModel


def download_form(request, file_name):
    source_instance = SourceListModel.objects.get(file_name=file_name)

    if request.method == 'POST':
        for name, val in request.POST.items():
            print('%s: %s' % (name, val))

    field_labels, field_types = source_instance.get_meta()
    list_data = {
        'display_name': source_instance.display_name,
        'updated': source_instance.update_date,
        'field_data': list(zip(field_labels, field_types))
    }
    return render(request, 'email_gen/list-form-base.html', {'list_data': list_data})
