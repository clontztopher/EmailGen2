from django.test import TestCase
from django.core.files import File
from .upload_utils import save_list

from ..models.model_utils import get_models


class UploadTests(TestCase):

    def test_save_list(self):
        aptx_list_model, aptx_entity_model = get_models('aptx')
        with open('email_gen/tests/test-apprfile.txt', 'rb') as f:
            test_file = File(f)
            list_instance = save_list(list_type='aptx', file=test_file)
            entities = list_instance.entities.all()[:10]
            self.assertTrue(len(entities) == 10)
            self.assertTrue(all([isinstance(e, aptx_entity_model) for e in entities]))
