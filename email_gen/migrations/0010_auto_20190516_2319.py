# Generated by Django 2.2.1 on 2019-05-16 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_gen', '0009_auto_20190515_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='lic_date_exp',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='lic_date_orig',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='trec_date_app_expires',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='trec_date_app_received',
            field=models.DateField(blank=True, null=True),
        ),
    ]
