from django.urls import path

from .list_upload.upload_views import upload_list, list_config, list_save
from .list_filter.list_filter_views import download_form
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', upload_list, name="upload"),
    path('list-config/<str:file_name>/', list_config, name="list_config"),
    path('list-save/', list_save, name="list_save"),
    path('download-form/<str:file_name>/', download_form, name="download_form")
]
