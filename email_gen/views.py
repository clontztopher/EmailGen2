from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # file_list = SourceListFileModel.objects.all()
    # return render(request, 'index.html', {'file_list': file_list})
    return render(request, 'index.html')
