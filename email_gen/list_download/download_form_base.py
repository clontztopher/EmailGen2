from django import forms
from ..constants import TREC_COUNTY_CODES_BY_REGION


class SourceListFilterForm(forms.Form):
    file_name = forms.CharField(max_length=40)
    file_name.widget.attrs.update({'class': 'form-control'})

    email_domains = forms.CharField(max_length=50, required=False)
    email_domains.widget.attrs.update({'class': 'form-control'})

    email_domains_inclusive = forms.BooleanField(required=False, initial=False)
    email_domains_inclusive.widget.attrs.update({'class': 'form-check-input'})

    def get_data(self, post_data={}):
        data = self.cleaned_data

        email_domains = post_data.get('email_domains')

        if email_domains:
            data['email_domains'] = [d.strip() for d in email_domains.split(',')]

        data['exp_dates'] = [d for n, d in post_data.items() if 'exp_indie_date' in n and d is not '']

        counties = data.get('counties', [])
        regions = data.get('regions')

        if regions:
            for region in regions:
                counties.extend(TREC_COUNTY_CODES_BY_REGION[region])

        data['county_codes'] = list(set(counties))

        return data
