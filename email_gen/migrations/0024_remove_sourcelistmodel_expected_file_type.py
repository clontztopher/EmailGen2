# Generated by Django 2.2.2 on 2019-06-13 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_gen', '0023_sourcelistmodel_encoding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sourcelistmodel',
            name='expected_file_type',
        ),
    ]
