from django import forms


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
