# Generated by Django 2.2.1 on 2019-05-14 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_gen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sourcelistmodel',
            name='field_types',
        ),
    ]
