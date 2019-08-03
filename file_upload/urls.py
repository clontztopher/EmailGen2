from django.urls import path
from .views import upload_list

urlpatterns = [
    path('', upload_list, name='upload_list')
]
