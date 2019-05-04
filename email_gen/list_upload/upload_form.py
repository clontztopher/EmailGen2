from django import forms


class SourceListUploadForm(forms.Form):
    # TYPES = [
    #     ('retx', 'Real Estate - Texas'),
    #     ('reok', 'Real Estate - Oklahoma'),
    #     ('retxprep', 'Real Estate Prep - Texas'),
    #     ('intx', 'Inspection - Texas'),
    #     ('aptx', 'Appraisal - Texas')
    # ]
    #
    # list_type = forms.ChoiceField(choices=TYPES)
    # list_type.widget.attrs.update({'class': 'form-control'})

    file = forms.FileField()
    file.widget.attrs.update({'class': 'form-control-file'})
