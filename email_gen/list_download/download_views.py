from django.shortcuts import render
from django.http import HttpResponse

from .download_utils import get_form_for


def download_form(request, file_type: str):
    form = get_form_for(file_type)

    if request.method == 'POST':
        loaded_form = form(request.POST)

        if loaded_form.is_valid():
            download_file_name = loaded_form.cleaned_data['file_name']
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=' + download_file_name + '.csv'

            # query_set = AppraiserTexas.objects.all()
            # response = download_list(query_set, response)

            return response

    return render(request, 'email_gen/list-form-base.html', {'form': form})
