from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SourceListModel


@login_required
def index(request):
    file_list = SourceListModel.objects.all()
    return render(request, 'index.html', {'file_list': file_list})
