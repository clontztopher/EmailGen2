# Generated by Django 2.1.7 on 2019-05-04 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_gen', '0011_auto_20190503_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestatetexaspreplistmodel',
            name='display_name',
            field=models.CharField(default='Real Estate License Applications - Texas', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='realestatetexaspreplistmodel',
            name='list_type',
            field=models.CharField(default='retxprep', editable=False, max_length=100),
        ),
    ]
