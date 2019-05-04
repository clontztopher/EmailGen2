from django.shortcuts import render
from .upload_form import SourceListUploadForm
from .upload_utils import save_list


def upload_list(request, list_type='retx'):
    instance = None
    if request.method == 'POST':
        form = SourceListUploadForm(request.POST, request.FILES)
        if form.is_valid():
            list_type = form.cleaned_data['list_type']
            instance = save_list(list_type, request.FILES['file'])

    form = SourceListUploadForm(initial={'type': list_type})
    return render(request, 'email_gen/upload-form.html', {'form': form, 'instance': instance})
