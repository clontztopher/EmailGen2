from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .upload_form import SourceListUploadForm
from ..file_storage.file_storage import FileStorageService
from ..list_save.save_list import save_source


@login_required
def upload_list(request):
    if request.method == 'POST':
        form = SourceListUploadForm(request.POST, request.FILES)

        if form.is_valid():
            list_id = form.cleaned_data['list_id']
            storage_service = FileStorageService(list_id)
            storage_service.save_file(request.FILES['file'])
            reader = storage_service.get_reader_from_stream()
            save_source(list_id, reader)

            # Return JSON for POST AJAX request
            return JsonResponse({'message': 'success'})

    # Return form template for GET request
    form = SourceListUploadForm()
    return render(request, 'email_gen/upload-form.html', {'form': form})
