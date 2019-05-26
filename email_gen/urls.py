from django.urls import path
from .views import index, fetch_and_save
from .list_filter.list_filter_views import download_form
from .file_storage.file_storage_api import save_source
from .list_save.list_save_api import list_save
from .list_upload.upload_views import upload_list

urlpatterns = [
    path('', index, name="index"),
    # API endpoint
    path('fetch-save/<str:file_id>/', fetch_and_save, name="fetch_save"),
    path('save-source/<str:file_id>/', save_source, name="save_source"),
    path('save-list/<str:file_id>/', list_save, name="list_save"),
    path('upload/', upload_list, name="upload_list"),
    # Download View
    path('download-form/<str:file_id>/', download_form, name="download_form")
]
