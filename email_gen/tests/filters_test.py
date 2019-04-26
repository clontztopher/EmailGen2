import datetime
from django.test import TestCase
from ..operations import predicates
from email_gen.constants import ITEMS, INCLUSIVE, DOMAINS, TREC_COUNTY_CODES_BY_REGION


class ListParserTests(TestCase):

    def test_in_list_insensitive_truthy(self):
        opts = {
            ITEMS: ['test', 'one', 'two', 'three']
        }
        self.assertTrue(predicates.in_list_insensitive(opts)('TEST'))

    def test_in_list_insensitive_falsey(self):
        opts = {
            ITEMS: ['test', 'one', 'two', 'three']
        }
        result = predicates.in_list_insensitive(opts)('four')
        self.assertFalse(result)

    def test_email_domains_truthy(self):
        opts = {
            DOMAINS: '@hotmail, @aol'
        }
        result = predicates.email_domains(opts)('jimmy@hotmail.com')
        self.assertTrue(result)

    def test_email_domain_falsey(self):
        opts = {
            DOMAINS: '@hotmail, @aol'
        }
        result = predicates.email_domains(opts)('susan@gmail.com')
        self.assertFalse(result)

    def test_email_domain_uppercase(self):
        opts = {
            DOMAINS: '@gmail, @aol',
            INCLUSIVE: True
        }
        result = predicates.email_domains(opts)('SUSAN@GMAIL.COM')
        self.assertTrue(result)

    def test_email_domains_empty(self):
        opts = {
            DOMAINS: '@hotmail',
            INCLUSIVE: True
        }
        result = predicates.email_domains(opts)('')
        self.assertFalse(result)

    def test_exp_date(self):
        opts = {
            'date': datetime.datetime(2019, 4, 18).date(),
            'format': '%m-%d-%Y',
        }
        result = predicates.exp_date_filter(opts)('04-18-2019')
        self.assertTrue(result, opts['date'])

    def test_county_filter(self):
        opts = {
            'counties': ['227'],
            'regions': []
        }
        test = predicates.trec_county_filter(opts)
        self.assertTrue(test('227'))
        self.assertFalse(test('228'))

    def test_county_filter_with_regions(self):
        opts = {
            'counties': [],
            'regions': ['Austin']
        }
        test = predicates.trec_county_filter(opts)
        self.assertTrue(test('011'))
        self.assertTrue(test('026'))
        self.assertFalse(test('005'))

    def test_county_filter_counties_and_regions(self):
        opts = {
            'counties': ['227'],
            'regions': ['Houston', 'San Antonio']
        }
        test = predicates.trec_county_filter(opts)
        self.assertTrue(test('227'))
        self.assertTrue(test('29'))
        self.assertTrue(test('000029'))
        self.assertTrue(test('000064'))
        self.assertFalse(test('000083'))
