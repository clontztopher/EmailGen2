import pandas as pd
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from email_gen.forms.get_form_for import get_form_for
from email_gen.forms.upload.upload import SourceListUploadForm
from .models.source import SourceListFileModel
from .operations.validator import make_processor


def index(request):
    file_list = SourceListFileModel.objects.all()
    return render(request, 'index.html', {'file_list': file_list})


def upload(request):
    if request.method == 'POST':
        form = SourceListUploadForm(request.POST, request.FILES)
        if form.is_valid():
            SourceListFileModel.save_file(request.POST['type'], request.FILES['file'])

    form = SourceListUploadForm()
    return render(request, 'email_gen/upload-form.html', {'form': form})


def delete(request, file_id):
    instance = SourceListFileModel.objects.get(pk=file_id)
    instance.delete()
    return HttpResponseRedirect(redirect_to='/')


def download_form(request, file_type: str):
    file_instance = SourceListFileModel.get_instance(file_type)
    form = get_form_for(file_type)

    if request.method == 'POST':
        loaded_form = form(request.POST)

        if loaded_form.is_valid():
            download_file_name = loaded_form.cleaned_data['file_name']

            opts = file_instance.config.get_reader_opts()
            file_reader = pd.read_csv(file_instance.file.path, **opts)
            process = make_processor(file_type, loaded_form.get_data(request.POST))

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=' + download_file_name + '.csv'

            write_header = True
            for chunk in file_reader:
                chunk = process(chunk)
                chunk.to_csv(path_or_buf=response, chunksize=100000, mode='a', header=write_header)
                write_header = False

            return response

    return render(request, 'email_gen/list-form-base.html', {'form': form, 'file': file_instance})
