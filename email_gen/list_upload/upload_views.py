from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .upload_form import SourceListUploadForm
from ..file_storage.file_storage import FileStorageService
from ..list_save.save_list import save_list


@login_required
def upload_list(request):
    if request.method == 'POST':
        form = SourceListUploadForm(request.POST, request.FILES)

        if form.is_valid():
            storage_service = FileStorageService()
            file_id = form.cleaned_data['list_id']
            blob = storage_service.get_blob(file_id)
            blob.upload_from_file(request.FILES['file'])
            save_list(file_id)

            # Return JSON for POST AJAX request
            return JsonResponse({'message': 'success'})

    # Return form template for GET request
    form = SourceListUploadForm()
    return render(request, 'email_gen/upload-form.html', {'form': form})
