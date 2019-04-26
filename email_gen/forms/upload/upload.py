from django import forms


# from email_gen.models.source import SourceListFileModel

class SourceListUploadForm(forms.Form):
    TYPES = [
        ('retx', 'Real Estate - Texas'),
        ('reok', 'Real Estate - Oklahoma'),
        ('repreptx', 'Real Estate Prep - Texas'),
        ('intx', 'Inspection - Texas'),
        ('aptx', 'Appraisal - Texas')
    ]

    type = forms.ChoiceField(choices=TYPES)
    type.widget.attrs.update({'class': 'form-control'})

    file = forms.FileField()
    file.widget.attrs.update({'class': 'form-control-file'})

# class SourceListUploadForm(forms.ModelForm):
# class Meta:
#     model = SourceListFileModel
#     fields = ['type', 'file']
#     widgets = {
#         'type': forms.Select(attrs={'class': 'form-control'}),
#         'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
#     }
