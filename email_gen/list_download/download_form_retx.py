from django import forms
from .download_form_base import SourceListFilterForm
from ..constants import TREC_COUNTY_CODES, TREC_COUNTY_CODES_BY_REGION, TREC_LIC_STATUS, TREC_LIC_TYPES, \
    TREC_ED_STATUS, TREC_MCE_STATUS


class TrecFilterForm(SourceListFilterForm):
    # License Type Field
    lic_type = forms.MultipleChoiceField(choices=TREC_LIC_TYPES, required=False)
    lic_type.widget.attrs.update({'class': 'form-control'})

    # License Status Field
    lic_status = forms.MultipleChoiceField(choices=TREC_LIC_STATUS, required=False)
    lic_status.widget.attrs.update({'class': 'form-control'})

    # SAE Education Status Field
    sae_status = forms.MultipleChoiceField(choices=TREC_ED_STATUS, required=False)
    sae_status.widget.attrs.update({'class': 'form-control'})

    # CE Education Status Field
    ce_status = forms.MultipleChoiceField(choices=TREC_MCE_STATUS, required=False)
    ce_status.widget.attrs.update({'class': 'form-control'})

    # License Expiration Date Fields
    exp_date_range_min = forms.DateField(widget=forms.SelectDateWidget, required=False)
    exp_date_range_max = forms.DateField(widget=forms.SelectDateWidget, required=False)

    # Designated Supervisor
    des_supervisor = forms.BooleanField(required=False, initial=False)
    des_supervisor.widget.attrs.update({'class': 'form-check-input'})

    # County codes field
    counties = forms.MultipleChoiceField(choices=[
        (code, county.title()) for code, county in TREC_COUNTY_CODES.items()
    ], required=False)
    counties.widget.attrs.update({'class': 'form-control'})

    # Regions manually collected based on county codes
    regions = forms.MultipleChoiceField(choices=[
        (region, region) for region in TREC_COUNTY_CODES_BY_REGION.keys()
    ], required=False)
    regions.widget.attrs.update({'class': 'form-control'})
