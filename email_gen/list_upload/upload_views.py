from django.shortcuts import render
from .upload_form import SourceListUploadForm
from .upload_utils import save_list


def upload_list(request, file_type='retx'):
    instance = None
    if request.method == 'POST':
        form = SourceListUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = save_list(request.POST['type'], request.FILES['file'])

    form = SourceListUploadForm(initial={'type': file_type})
    return render(request, 'email_gen/upload-form.html', {'form': form, 'instance': instance})
