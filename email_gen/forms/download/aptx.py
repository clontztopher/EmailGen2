from django import forms
from .filter import SourceListFilterForm
from ...constants import TREC_COUNTY_CODES, TREC_COUNTY_CODES_BY_REGION


class ApTxFilterForm(SourceListFilterForm):
    LIC_TYPES = [
        ('APCR', 'Certified Residential Appraiser'),
        ('APGN', 'Certified General Appraiser'),
        ('APOS', 'Temporary Out of State Appraiser'),
        ('APPV', 'Provisional Licensed Appraiser'),
        ('APSC', 'Licensed Residential Appraiser'),
        ('APTR', 'Appraiser Trainee')
    ]

    LIC_STATUS = [
        ('20', 'Current and Active'),
        ('21', 'Current and Inactive'),
        ('30', 'Probation and Active'),
        ('31', 'Probation and Inactive'),
        ('45', 'Expired'),
        ('47', 'Suspended'),
        ('56', 'Relinquished'),
        ('57', 'Revoked'),
        ('80', 'Deceased')
    ]

    # License Type Field
    lic_type = forms.MultipleChoiceField(choices=LIC_TYPES, required=False)
    lic_type.widget.attrs.update({'class': 'form-control'})

    # License Status Field
    lic_status = forms.MultipleChoiceField(choices=LIC_STATUS, required=False)
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
