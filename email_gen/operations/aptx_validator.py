def make_aptx_validator(form_data):
    pass
# Add data for individual date
# if 'exp_indie_date' in field_name:
#     validator.add_filter(
#         field_name='exp_date',
#         predicate='individual_date',
#         date=datetime.strptime(field_data, '%Y-%m-%d').strftime('%m-%d-%Y')
#     )

# Add data for date range
# if 'exp_date_range' in field_name:
#     validator.add_filter(
#         field_name='exp_date',
#         predicate='date_range',
#         filter_type='all',
#         date=datetime.strptime(field_data, '%Y-%m-%d'),
#         limit=field_name[-3:],
#         format='%m-%d-%Y'
#     )

# if 'email_domains' == field_name:
#     validator.add_filter(
#         predicate='email_domains',
#         field_name='email',
#         domains=field_data,
#         inclusive=form_data['email_domains_inclusive']
#     )

# if 'lic_type' in form_data and form_data['lic_type']:
#     lic_type_filter = filters.CaseInsensitiveListCheck('lic_type')
#     lic_type_filter.add_checklist(form_data['lic_type'])
#
# if 'lic_status' == field_name:
#     validator.add_filter(
#         predicate='in_list_case_insensitive',
#         field_name='lic_status',
#         check_list=field_data
#     )
#
# if 'counties' == field_name:
#     validator.add_filter(
#         predicate='trec_county_filter',
#         field_name='mail_county',
#         counties=field_data
#     )
#
# if 'regions' == field_name:
#     validator.add_filter(
#         predicate='trec_region_filter',
#         field_name='mail_county',
#         regions=field_data
#     )
#
# return validator
