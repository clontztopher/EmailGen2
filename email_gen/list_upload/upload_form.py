from django import forms


class SourceListUploadForm(forms.Form):
    list_name = forms.CharField(max_length=40)
    list_name.widget.attrs.update({'class': 'form-control'})

    file = forms.FileField()
    file.widget.attrs.update({'class': 'form-control-file'})
