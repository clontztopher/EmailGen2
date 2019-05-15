from django.shortcuts import render
from ..models import SourceListModel

from django.forms.models import model_to_dict
from django.forms import MultipleChoiceField

from ..constants import LICENSE_TYPES
from ..list_filter.list_filter import PersonFilter
from ..models import Person


def download_form(request, file_name):
    # source_instance = SourceListModel.objects.get(file_name=file_name)

    # if request.method == 'POST':
    #     query_params = {}
    #
    #     for name, val in request.POST.items():
    #         if name == 'csrfmiddlewaretoken':
    #             continue
    #
    #         label, data_type, opt = name.split('-')
    #
    #         if not query_params.get(label):
    #             query_params[label] = {opt: val, 'data_type': data_type}
    #         else:
    #             query_params[label][opt] = val
    #
    #     query_params = {label: opts for label, opts in query_params.items() if opts.get('value')}
    #
    #     query_set = source_instance.people.all()
    #
    #     for label, opts in query_params.items():
    #         if opts['data_type'] == 'text':
    #             if opts['exact'] == '1':
    #                 query_set = query_set.filter(**{label: opts['value']})
    #             else:
    #                 query_set = query_set.filter(**{label + '__icontains': opts['value']})
    #
    #     for person in query_set:
    #         print(str(model_to_dict(person)))

    # field_labels = source_instance.get_meta()
    #
    # list_data = {
    #     'display_name': source_instance.display_name,
    #     'updated': source_instance.update_date,
    #     'field_labels': field_labels
    # }

    f = PersonFilter(request.GET, queryset=Person.objects.all())
    # return render(request, 'email_gen/list-form-base.html', {'list_data': list_data, 'test_field': test_field})
    return render(request, 'email_gen/list-form-base.html', {'filter': f})
