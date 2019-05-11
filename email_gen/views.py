from django.shortcuts import render

from .models import SourceListModel


def index(request):
    file_list = SourceListModel.objects.all()
    return render(request, 'index.html', {'file_list': file_list})
