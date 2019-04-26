from django.core.files import File
from ..models.source import SourceListFileModel


def get_upload_test(type):
    with open('email_gen/tests/test-apprfile.txt', 'rb') as f:
        test_file = File(f)
        model_instance = SourceListFileModel.save_file(
            type=type, file=test_file)
        return model_instance
