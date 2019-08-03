from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import SourceListView

urlpatterns = [
    path('', login_required(SourceListView.as_view()))
]
