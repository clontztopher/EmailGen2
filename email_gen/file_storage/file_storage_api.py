from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .file_storage import FileStorageService


@login_required
def save_source(request, file_id):
    """
    View responsible only for retrieving and saving files based on file_id
    """
    storage_service = FileStorageService(file_id)
    try:
        storage_service.fetch_and_save()
        return JsonResponse({'message': 'success'})
    except:
        return JsonResponse({'message': "No source data for list id '%s'" % file_id})
