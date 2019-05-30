from django.http import JsonResponse
from .save_list import save_list
from django.contrib.auth.decorators import login_required


@login_required
def list_save(request, file_id=None):
    """
    View responsible only for saving data from source file to database
    """
    save_list(file_id)
    return JsonResponse({'message': 'success'})
