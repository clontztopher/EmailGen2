from django.http import JsonResponse
from .save_list import save_list
from ..file_storage import FileStorageService
from django.contrib.auth.decorators import login_required


@login_required
def list_save(request, file_id=None):
    """
    View responsible only for saving data from source file to database
    """
    storage_service = FileStorageService()
    reader = storage_service.get_reader_from_stream(file_id)
    save_list(file_id, reader)
    return JsonResponse({'message': 'success'})
