from django import forms
from .download_form_base import SourceListFilterForm


class RealEstatePrepTexasForm(SourceListFilterForm):
    # Applicaton Type Field
    lic_type = forms.MultipleChoiceField(choices=[('BRK', 'Broker'), ('SALE', 'Sales Agent')], required=False)
    lic_type.widget.attrs.update({'class': 'form-control'})

    # License Expiration Date Fields
    exp_date_range_min = forms.DateField(widget=forms.SelectDateWidget, required=False)
    exp_date_range_max = forms.DateField(widget=forms.SelectDateWidget, required=False)
