from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import SourceListModel
from .file_storage import FileStorageService
from .list_save.save_list import save_source


@login_required
def index(request):
    file_list = SourceListModel.objects.order_by('display_name')
    return render(request, 'index.html', {'file_list': file_list})


@login_required
def fetch_and_save(request, file_id):
    """
    View that both retrieves file, saves file,
    and saves file data to database
    """
    storage_service = FileStorageService(file_id)
    try:
        storage_service.fetch_and_save()
        reader = storage_service.get_reader_from_stream()
        updated_date = save_source(file_id, reader)
        return JsonResponse({'message': 'success', 'updated': updated_date.strftime('%b %d, %Y')})
    except:
        return JsonResponse({'message': "Unable to fetch and save list."})
