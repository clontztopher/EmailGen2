import os
from django.test import TestCase
# from ..models import SourceListFileModel
from .fixtures import get_upload_test


class SourceListFileModelTests(TestCase):
    TEST_LINE = ['APCR', '1360675', 'Kelly Michelle Ruoff', '', '20', '11-27-2017', '11-30-2019', 'kruoff101@gmail.com',
                 '(315) 491-6440', '18 Ridge Dr', '', '', 'HICKORY CREEK', 'TX', '75065', '61', '1000000100', 'N']

    def test_file_is_uploaded_and_model_created(self):
        instance = get_upload_test('aptx')
        file_exists = os.path.isfile(instance.file.path)
        self.assertTrue(file_exists)
        os.remove(instance.file.path)

    def test_deleting_model_removes_file(self):
        instance = get_upload_test('aptx')
        file_path = instance.file.path
        instance.delete()
        file_exists = os.path.isfile(file_path)
        self.assertFalse(file_exists)

    def test_uploading_file_with_same_name_replaces_old(self):
        instance_1 = get_upload_test('aptx')
        instance_2 = get_upload_test('aptx')
        self.assertEqual(instance_1.file.name, instance_2.file.name)
        instance_2.delete()

    def test_uploading_file_with_same_name_updates_model(self):
        instance_1 = get_upload_test('aptx')
        instance_2 = get_upload_test('aptx')
        self.assertEqual(instance_1.pk, instance_2.pk)
        instance_2.delete()

    def test_get_display_name_is_correct(self):
        instance = get_upload_test('aptx')
        self.assertEqual(instance.get_type_display(), 'Appraisal - Texas')

    def test_get_row_dict(self):
        instance = get_upload_test('aptx')
        entity = instance.zip_row(self.TEST_LINE)
        self.assertTrue(entity['lic_type'], 'APCR')
