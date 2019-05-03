from django.urls import path

from .list_upload.upload_views import upload_list
from .list_download.download_views import download_form
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', upload_list, name="upload"),
    path('upload/<str:file_type>/', upload_list, name="upload"),
    path('download/<str:file_type>/', download_form, name="download_form")
]
