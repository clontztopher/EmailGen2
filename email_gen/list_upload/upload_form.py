from django import forms
from ..models import SourceListModel


class SourceListUploadForm(forms.Form):
    list_id = forms.ChoiceField(choices=SourceListModel.get_list_options)
    list_id.widget.attrs.update({'class': 'form-control'})

    file = forms.FileField()
    file.widget.attrs.update({'class': 'form-control-file'})
