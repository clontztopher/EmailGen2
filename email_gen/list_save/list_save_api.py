from django.http import JsonResponse
from .save_list import save_source
from ..file_storage import FileStorageService
from django.contrib.auth.decorators import login_required


@login_required
def list_save(request, file_id):
    """
    View responsible only for saving data from source file to database
    """
    storage_service = FileStorageService(file_id)
    reader = storage_service.get_reader_from_stream()
    save_source(file_id, reader)
    return JsonResponse({'message': 'success'})
