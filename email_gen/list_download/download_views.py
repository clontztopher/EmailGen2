from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

from .download_utils import get_form_for
from ..models.model_utils import get_models


def download_form(request, file_type: str):
    form = get_form_for(file_type)
    list_model, list_entity = get_models(file_type)
    list_instance = list_model.objects.get(list_type=file_type)

    if request.method == 'POST':
        loaded_form = form(request.POST)

        if loaded_form.is_valid():
            # Create csv http response object
            download_file_name = loaded_form.cleaned_data['file_name']
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=%s.csv' % download_file_name

            # Get processed form data
            post_data = loaded_form.get_data(post_data=request.POST)

            # Build a query based on processed data
            query_set = list_entity.objects.all()

            if post_data.get('exp_dates'):
                import datetime
                exp_dates = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in post_data['exp_dates']]
                query_set = query_set.filter(exp_date__in=exp_dates)
            elif post_data.get('exp_date_range_min') or post_data.get('exp_date_range_max'):
                query_set = query_set.filter(exp_date__range=(
                    post_data['exp_date_range_min'],
                    post_data['exp_date_range_max']
                ))

            if post_data.get('email_domains'):
                if post_data['email_domains_inclusive']:
                    for domain in post_data['email_domains']:
                        query_set = query_set.filter(email__icontains=domain)
                else:
                    for domain in post_data['email_domains']:
                        query_set = query_set.exclude(email__icontains=domain)

            if post_data.get('counties'):
                query_set = query_set.filter(mail_county__in=post_data['counties'])

            # Execute query and download results as csv
            query_result = list(query_set.values())
            list_headers = list_model.FILE_HEADERS
            df = pd.DataFrame(query_result, columns=list_headers)
            df.fillna('')
            df.to_csv(path_or_buf=response, mode='a')

            return response

    return render(request, 'email_gen/list-form-base.html', {'form': form, 'file': list_instance})
