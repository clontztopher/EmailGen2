from django.views.generic.list import ListView
from .models import SourceListModel


class SourceListView(ListView):
    model = SourceListModel
    template_name = 'email_gen/source-lists.html'
    ordering = 'display_name'
