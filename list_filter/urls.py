from django.urls import path
from .views import download_form

urlpatterns = [
    path('<str:file_id>/', download_form, name='download_form')
]
