# Generated by Django 2.2.1 on 2019-05-14 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SourceListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=60)),
                ('display_name', models.CharField(default='Uploaded List', max_length=60)),
                ('update_date', models.DateField(auto_now=True)),
                ('field_labels', models.CharField(blank=True, max_length=1000)),
                ('field_types', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(blank=True, max_length=180)),
                ('firstname', models.CharField(blank=True, max_length=60)),
                ('middlename', models.CharField(blank=True, max_length=60)),
                ('lastname', models.CharField(blank=True, max_length=60)),
                ('suffix', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address_1', models.CharField(blank=True, max_length=200)),
                ('address_2', models.CharField(blank=True, max_length=200)),
                ('address_3', models.CharField(blank=True, max_length=200)),
                ('address_4', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zip', models.CharField(blank=True, max_length=20)),
                ('trec_county', models.CharField(blank=True, max_length=3)),
                ('county', models.CharField(blank=True, max_length=200)),
                ('lic_number', models.CharField(blank=True, max_length=20)),
                ('lic_status', models.CharField(choices=[('N/A', 'Not Available'), ('ACT', 'Active'), ('INA', 'Inactive'), ('EXP', 'Expired'), ('SUS', 'Suspended'), ('REL', 'Relinquished'), ('REV', 'Revoked'), ('DEC', 'Deceased')], default='N/A', max_length=5)),
                ('lic_type', models.CharField(blank=True, choices=[('SALE', 'TREC - Sales Agent'), ('BRK', 'TREC - Individual Broker'), ('BLLC', 'TREC - Limited Liability Corporation Broker'), ('BCRP', 'TREC - Corporation Broker'), ('6', 'TREC - Partnership Broker'), ('REB', 'TREC - Broker Organization Branch'), ('PRIN', 'TREC - Professional Inspector'), ('REIN', 'TREC - Real Estate Inspector'), ('APIN', 'TREC - Apprentice Inspector'), ('ILLC', 'TREC - Professional Inspector, LLC'), ('ICRP', 'TREC - Professional Inspector, Corporation'), ('ERWI', 'TREC - Easement and Right-of-Way, Individual'), ('ERWO', 'TREC - Easement and Right-of-Way, Business'), ('APCR', 'TALCB - Certified Residential Appraiser'), ('APGN', 'TALCB - Certified General Appraiser'), ('APOS', 'TALCB - Temporary Out of State Appraiser'), ('APPV', 'TALCB - Provisional Licensed Appraiser'), ('APSC', 'TALCB - Licensed Residential Appraiser'), ('APTR', 'TALCB - Appraiser Trainee'), ('BR', 'OREC - Broker'), ('SA', 'OREC - Sales Associate'), ('PS', 'OREC - Provisional Sales Associate')], max_length=5)),
                ('lic_date', models.DateField(null=True)),
                ('lic_exp', models.DateField(null=True)),
                ('trec_app_received', models.DateField(null=True)),
                ('trec_app_expires', models.DateField(null=True)),
                ('trec_ed_status', models.CharField(blank=True, choices=[('0', 'No Non-elective CE Requirement'), ('1', 'Non-elective CE Requirements Outstanding'), ('2', 'Non-elective CE Requirements Met')], max_length=1)),
                ('trec_mce_status', models.CharField(blank=True, choices=[('0', 'No MCE Requirement'), ('1', 'MCE Requirements Outstanding'), ('2', 'MCE Requirements Met')], max_length=1)),
                ('designated_supervisor', models.BooleanField(default=False)),
                ('source_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people', to='email_gen.SourceListModel')),
            ],
        ),
    ]
