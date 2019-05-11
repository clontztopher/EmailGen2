# from django.shortcuts import render
# from django.http import HttpResponse
# import pandas as pd
#
# from .download_utils import get_form_for
#
#
# def download_form(request, file_type: str):
#     form = get_form_for(file_type)
#     list_model, list_entity = get_models(file_type)
#     list_instance = list_model.objects.get(list_type=file_type)
#
#     if request.method == 'POST':
#         loaded_form = form(request.POST)
#
#         if loaded_form.is_valid():
#             # Create csv http response object
#             download_file_name = loaded_form.cleaned_data['file_name']
#             response = HttpResponse(content_type='text/csv')
#             response['Content-Disposition'] = 'attachment; filename=%s.csv' % download_file_name
#
#             # Get processed form data and query set
#             post_data = loaded_form.get_data(post_data=request.POST)
#             query_set = list_entity.objects.all()
#
#             query_result = QueryBuilder.execute_query(query_set, post_data)
#
#             list_headers = list_model.FILE_HEADERS
#             df = pd.DataFrame(query_result, columns=list_headers)
#             df.fillna('')
#             df.to_csv(path_or_buf=response, mode='a')
#
#             return response
#
#     return render(request, 'email_gen/list-form-base.html', {'form': form, 'file': list_instance})
