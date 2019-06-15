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
            file = request.FILES['file']
            list_id = form.cleaned_data['list_id']
            storage_service = FileStorageService()
            storage_service.store_file(file.read(), file.name, list_id)
            reader = storage_service.stream_reader(list_id)
            save_source(list_id, reader)

            # Return JSON for POST AJAX request
            return JsonResponse({'message': 'success'})

    # Return form template for GET request
    form = SourceListUploadForm()
    return render(request, 'email_gen/upload-form.html', {'form': form})
