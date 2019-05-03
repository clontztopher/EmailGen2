from django import forms
from .download_form_base import SourceListFilterForm
from ..constants import TREC_COUNTY_CODES, TREC_COUNTY_CODES_BY_REGION, APTX_LIC_STATUS, APTX_LIC_TYPES


class ApTxFilterForm(SourceListFilterForm):
    # License Type Field
    lic_type = forms.MultipleChoiceField(choices=APTX_LIC_TYPES, required=False)
    lic_type.widget.attrs.update({'class': 'form-control'})

    # License Status Field
    lic_status = forms.MultipleChoiceField(choices=APTX_LIC_STATUS, required=False)
    lic_status.widget.attrs.update({'class': 'form-control'})

    # License Expiration Date Fields
    exp_date_range_min = forms.DateField(widget=forms.SelectDateWidget, required=False)
    exp_date_range_max = forms.DateField(widget=forms.SelectDateWidget, required=False)

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
