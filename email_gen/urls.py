from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', views.upload, name="upload"),
    path('upload/<str:file_type>/', views.upload, name="upload"),
    path('delete/<str:file_type>/', views.delete, name="delete"),
    path('download/<str:file_type>/', views.download_form, name="download_form")
]
