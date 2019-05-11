from django.urls import path

from .list_upload.upload_views import upload_list, list_config, list_save
# from .list_download.download_views import download_form
# from .list_filter.filter_views import person_filter
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', upload_list, name="upload"),
    path('list-config/<str:file_name>/', list_config, name="list_config"),
    path('list-save/', list_save, name="list_save"),
    # path('upload/<str:file_type>/', upload_list, name="upload"),
    # path('download/<str:file_type>/', download_form, name="download_form"),
    # path('list-filter/', person_filter, name="list_filter")
]
