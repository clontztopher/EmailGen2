# Generated by Django 2.2.2 on 2019-06-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_gen', '0021_auto_20190526_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcelistmodel',
            name='expected_file_type',
            field=models.CharField(choices=[('zip', 'zip'), ('txt', 'txt'), ('csv', 'csv')], default='zip', max_length=3),
        ),
    ]
