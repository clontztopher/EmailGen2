from django.test import TestCase, Client
from .models import SourceListModel
from .save_list import save_source


class TestFileSave(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_save_file_inspector(self):
        source_instance = SourceListModel.objects.create(
            file_id='intx',
            display_name='Inspector - TX',
            source_url='https://www.trec.texas.gov/sites/default/files/high-value-data-sets/inspfile.zip',
            zip_file_name='inspfile.txt',
            field_labels='lic_type::lic_number::fullname::suffix::lic_status::lic_date_orig::lic_date_exp'
                         '::trec_ed_status::trec_mce_status::designated_supervisor::phone::email::address_2'
                         '::address_3::address_4::city::state::zip::county'
        )
        save_source('intx')
        self.assertTrue(source_instance.inspectortexas_set.count() > 1000)

    def test_save_file_appraiser_tx(self):
        source_instance = SourceListModel.objects.create(
            file_id='aptx',
            display_name='Appraiser - TX',
            source_url='https://www.trec.texas.gov/sites/default/files/high-value-data-sets/apprfile.zip',
            zip_file_name='apprfile.txt',
            field_labels='lic_type::lic_number::fullname::suffix::lic_status::lic_date_orig::lic_date_exp::email'
                         '::phone::address_2::address_3::address_4::city::state::zip::county'
        )
        save_source('aptx')
        self.assertTrue(source_instance.appraisertexas_set.count() > 1000)

    def test_save_file_trec(self):
        source_instance = SourceListModel.objects.create(
            file_id='trec',
            display_name='Real Estate - TX',
            source_url='https://www.trec.texas.gov/sites/default/files/high-value-data-sets/trecfile.zip',
            zip_file_name='trecfile.txt',
            field_labels='lic_type::lic_number::fullname::suffix::lic_status::lic_date_orig::lic_date_exp'
                         '::trec_ed_status::trec_mce_status::designated_supervisor::email::phone::address_2'
                         '::address_3::address_4::city::state::zip::county'
        )
        save_source('trec')
        self.assertTrue(source_instance.realestatesalesagenttexas_set.count() > 100000)

    def test_save_file_txprep(self):
        source_instance = SourceListModel.objects.create(
            file_id='retx-prep',
            display_name='Real Estate Prep - TX',
            source_url='hhttps://www.trec.texas.gov/sites/default/files/high-value-data-sets/REIApplication.zip',
            zip_file_name='REIApplication.txt',
            field_labels='lic_type::app_date_orig::app_date_exp::lastname::firstname::middlename::suffix::address_2'
                         '::address_3::address_4::city::state::zip::phone::email'
        )
        save_source('retx-prep')
        self.assertTrue(source_instance.realestatesalesagentapplicanttexas_set.count() > 1000)
