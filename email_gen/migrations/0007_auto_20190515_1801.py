# Generated by Django 2.2.1 on 2019-05-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_gen', '0006_auto_20190514_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcelistmodel',
            name='display_name',
            field=models.CharField(default='Uploaded List', max_length=60, unique=True),
        ),
    ]