from django.urls import path
from django.contrib.auth.decorators import login_required
from .list_upload.upload_views import upload_list
from .list_filter.list_filter_views import download_form
from .views import SourceListView

urlpatterns = [
    path('', login_required(SourceListView.as_view())),
    path('upload/', upload_list, name='upload_list'),
    path('download-form/<str:file_id>/', download_form, name='download_form')
]
