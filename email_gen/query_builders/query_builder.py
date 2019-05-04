import datetime


class QueryBuilder:

    @classmethod
    def execute_query(cls, query_set, post_data):

        # Email Domains Query
        if post_data.get('email_domains'):

            if post_data['email_domains_inclusive']:
                for domain in post_data['email_domains']:
                    query_set = query_set.filter(email__icontains=domain)

            else:
                for domain in post_data['email_domains']:
                    query_set = query_set.exclude(email__icontains=domain)

        # License Expiration Date Query
        if post_data.get('exp_dates'):
            exp_dates = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in post_data['exp_dates']]
            query_set = query_set.filter(exp_date__in=exp_dates)

        elif post_data.get('exp_date_range_min') or post_data.get('exp_date_range_max'):
            query_set = query_set.filter(exp_date__range=(
                post_data['exp_date_range_min'],
                post_data['exp_date_range_max']
            ))

        # License Type Query Appraisal
        
        # Trec Counites Query
        if post_data.get('counties'):
            query_set = query_set.filter(mail_county__in=post_data['counties'])

        # Return executed query results
        return list(query_set.values())
