from django import forms
from ..models import SourceListModel


class SourceListUploadForm(forms.Form):
    existing_lists = forms.ChoiceField(choices=SourceListModel.get_list_options)
    existing_lists.widget.attrs.update({'class': 'form-control'})

    new_list = forms.CharField(max_length=40, label='New List', required=False)
    new_list.widget.attrs.update({'class': 'form-control'})

    file = forms.FileField()
    file.widget.attrs.update({'class': 'form-control-file'})
