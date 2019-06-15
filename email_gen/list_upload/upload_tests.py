import os
from django.test import TestCase, Client
from django.conf import settings
from django.contrib.auth.models import User


class UploadTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test')
        user.set_password('test')
        user.save()

        # TODO: Won't work without SourceListModel instances
        # to provide options for upload form

    def test_save_list(self):
        client = Client()
        client.login(username='test', password='test')
        file_path = os.path.join(settings.MOCK_FILE_LOCATION, 'inspfile.txt')
        with open(file_path, 'r') as mock_file:
            res = client.post('/upload/', {
                'list_id': 'intx',
                'file': mock_file
            })
            print(str(res))
