from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .upload_form import SourceListUploadForm
from file_storage.storage_service import FileStorageService
from email_gen.save_list import save_source


@login_required
def upload_list(request):
    if request.method == 'POST':
        form = SourceListUploadForm(request.POST, request.FILES)

        if form.is_valid():
            # Get file from request
            file = request.FILES['file']
            list_id = form.cleaned_data['list_id']
            storage_service = FileStorageService()

            # Get bytes from file
            file_bytes = file.read()
            storage_service.store_file(file_bytes, file.name, list_id)
            reader = storage_service.stream_reader(list_id)
            save_source(list_id, reader)

            # Return JSON for POST AJAX request
            return JsonResponse({'message': 'success'})

    # Return form template for GET request
    form = SourceListUploadForm()
    return render(request, 'file_upload/upload-form.html', {'form': form})
