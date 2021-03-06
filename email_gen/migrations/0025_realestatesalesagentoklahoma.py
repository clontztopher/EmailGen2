# Generated by Django 2.2.2 on 2019-06-16 03:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('email_gen', '0024_remove_sourcelistmodel_expected_file_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealEstateSalesAgentOklahoma',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('firstname', models.CharField(blank=True, max_length=255, null=True)),
                ('middlename', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('suffix', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('address_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('address_3', models.CharField(blank=True, max_length=255, null=True)),
                ('address_4', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zip', models.CharField(blank=True, max_length=20, null=True)),
                ('county', models.CharField(blank=True, max_length=25, null=True)),
                ('lic_number', models.CharField(blank=True, max_length=20)),
                ('lic_status', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive')], max_length=1, null=True)),
                ('lic_type', models.CharField(blank=True, choices=[('BR', 'Broker'), ('SA', 'Sales Agent')], max_length=2, null=True)),
                ('lic_date_exp', models.DateField(blank=True, null=True)),
                ('source_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_gen.SourceListModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
