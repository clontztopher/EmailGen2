from django import forms
from .filter import SourceListFilterForm
from ...constants import TREC_COUNTY_CODES, TREC_COUNTY_CODES_BY_REGION


class TrecFilterForm(SourceListFilterForm):
    LIC_TYPES = [
        ('SALE', 'Sales Agent'),
        ('BRK', 'Individual Broker'),
        ('BLLC', 'Limited Liability Corporation Broker'),
        ('BCRP', 'Corporation Broker'),
        ('6', 'Partnership Broker'),
        ('REB', 'Broker Organization Branch'),
        ('PRIN', 'Professional Inspector'),
        ('REIN', 'Real Estate Inspector'),
        ('APIN', 'Apprentice Inspector'),
        ('ILLC', 'Professional Inspector, LLC'),
        ('ICRP', 'Professional Inspector, Corporation'),
        ('ERWI', 'Easement and Right-of-Way, Individual'),
        ('ERWO', 'Easement and Right-of-Way, Business')
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

    # Applies to everyone who is not CE so use for SAE
    EDUCATION_STATUS = [
        ('0', 'No Non-elective CE Requirement'),
        ('1', 'Non-elective CE Requirements Outstanding'),
        ('2', 'Non-elective CE Requirements Met')
    ]

    MCE_STATUS = [
        ('0', 'No MCE Requirement'),
        ('1', 'MCE Requirements Outstanding'),
        ('2', 'MCE Requirements Met')
    ]

    DESIGNATED_SUPERVISOR = [
        ('0', 'Not Designated Supervisor'),
        ('1', 'Designated Supervisor')
    ]

    # License Type Field
    lic_type = forms.MultipleChoiceField(choices=LIC_TYPES, required=False)
    lic_type.widget.attrs.update({'class': 'form-control'})

    # License Status Field
    lic_status = forms.MultipleChoiceField(choices=LIC_STATUS, required=False)
    lic_status.widget.attrs.update({'class': 'form-control'})

    # SAE Education Status Field
    sae_status = forms.MultipleChoiceField(choices=EDUCATION_STATUS, required=False)
    sae_status.widget.attrs.update({'class': 'form-control'})

    # CE Education Status Field
    ce_status = forms.MultipleChoiceField(choices=MCE_STATUS, required=False)
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
