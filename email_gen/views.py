from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import SourceListModel
from .file_storage import FileStorageService
from .list_save.save_list import save_source

from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def current_user(request):
    """
    Determine current user and get their data
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
def list_data(request):
    file_list = SourceListModel.objects \
        .order_by('display_name') \
        .values('file_id', 'display_name', 'update_date')

    return JsonResponse(list(file_list), safe=False)


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
