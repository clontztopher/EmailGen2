# Generated by Django 2.2.1 on 2019-05-25 04:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('email_gen', '0014_auto_20190525_0429'),
    ]

    operations = [
        migrations.CreateModel(
            name='TexasAppraiser',
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
                ('trec_county', models.CharField(blank=True, max_length=3, null=True)),
                ('county', models.CharField(blank=True, max_length=25, null=True)),
                ('lic_number', models.CharField(blank=True, max_length=20)),
                ('lic_status', models.CharField(blank=True, choices=[('20', 'Current and Active'), ('21', 'Current and Inactive'), ('30', 'Probation and Active'), ('31', 'Probation and Inactive'), ('45', 'Expired'), ('47', 'Suspended'), ('56', 'Relinquished'), ('57', 'Revoked'), ('80', 'Deceased')], max_length=255, null=True)),
                ('lic_type', models.CharField(blank=True, choices=[('APCR', 'TALCB - Certified Residential Appraiser'), ('APGN', 'TALCB - Certified General Appraiser'), ('APOS', 'TALCB - Temporary Out of State Appraiser'), ('APPV', 'TALCB - Provisional Licensed Appraiser'), ('APSC', 'TALCB - Licensed Residential Appraiser'), ('APTR', 'TALCB - Appraiser Trainee')], max_length=255, null=True)),
                ('lic_date_orig', models.DateField(blank=True, null=True)),
                ('lic_date_exp', models.DateField(blank=True, null=True)),
                ('source_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_gen.SourceListModel')),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateSalesAgentTexas',
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
                ('trec_county', models.CharField(blank=True, max_length=3, null=True)),
                ('county', models.CharField(blank=True, max_length=25, null=True)),
                ('lic_number', models.CharField(blank=True, max_length=20)),
                ('lic_status', models.CharField(blank=True, choices=[('20', 'Current and Active'), ('21', 'Current and Inactive'), ('30', 'Probation and Active'), ('31', 'Probation and Inactive'), ('45', 'Expired'), ('47', 'Suspended'), ('56', 'Relinquished'), ('57', 'Revoked'), ('80', 'Deceased')], max_length=255, null=True)),
                ('lic_type', models.CharField(blank=True, choices=[('SALE', 'TREC - Sales Agent'), ('BRK', 'TREC - Individual Broker'), ('BLLC', 'TREC - Limited Liability Corporation Broker'), ('BCRP', 'TREC - Corporation Broker'), ('6', 'TREC - Partnership Broker'), ('REB', 'TREC - Broker Organization Branch'), ('PRIN', 'TREC - Professional Inspector'), ('REIN', 'TREC - Real Estate Inspector'), ('APIN', 'TREC - Apprentice Inspector'), ('ILLC', 'TREC - Professional Inspector, LLC'), ('ICRP', 'TREC - Professional Inspector, Corporation'), ('ERWI', 'TREC - Easement and Right-of-Way, Individual'), ('ERWO', 'TREC - Easement and Right-of-Way, Business')], max_length=255, null=True)),
                ('lic_date_orig', models.DateField(blank=True, null=True)),
                ('lic_date_exp', models.DateField(blank=True, null=True)),
                ('trec_ed_status', models.CharField(blank=True, choices=[('0', 'No Non-elective CE Requirement'), ('1', 'Non-elective CE Requirements Outstanding'), ('2', 'Non-elective CE Requirements Met')], max_length=255, null=True)),
                ('trec_mce_status', models.CharField(blank=True, choices=[('0', 'No MCE Requirement'), ('1', 'MCE Requirements Outstanding'), ('2', 'MCE Requirements Met')], max_length=255, null=True)),
                ('designated_supervisor', models.CharField(blank=True, max_length=1, null=True)),
                ('source_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_gen.SourceListModel')),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateSalesAgentApplicantTexas',
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
                ('lic_type', models.CharField(blank=True, choices=[('SALE', 'TREC - Sales Agent'), ('BRK', 'TREC - Individual Broker'), ('BLLC', 'TREC - Limited Liability Corporation Broker'), ('BCRP', 'TREC - Corporation Broker'), ('6', 'TREC - Partnership Broker'), ('REB', 'TREC - Broker Organization Branch'), ('PRIN', 'TREC - Professional Inspector'), ('REIN', 'TREC - Real Estate Inspector'), ('APIN', 'TREC - Apprentice Inspector'), ('ILLC', 'TREC - Professional Inspector, LLC'), ('ICRP', 'TREC - Professional Inspector, Corporation'), ('ERWI', 'TREC - Easement and Right-of-Way, Individual'), ('ERWO', 'TREC - Easement and Right-of-Way, Business')], max_length=255, null=True)),
                ('app_date_orig', models.DateField(blank=True, null=True)),
                ('app_date_exp', models.DateField(blank=True, null=True)),
                ('source_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_gen.SourceListModel')),
            ],
        ),
        migrations.CreateModel(
            name='InspectorTexas',
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
                ('trec_county', models.CharField(blank=True, max_length=3, null=True)),
                ('county', models.CharField(blank=True, max_length=25, null=True)),
                ('lic_number', models.CharField(blank=True, max_length=20)),
                ('lic_status', models.CharField(blank=True, choices=[('20', 'Current and Active'), ('21', 'Current and Inactive'), ('30', 'Probation and Active'), ('31', 'Probation and Inactive'), ('45', 'Expired'), ('47', 'Suspended'), ('56', 'Relinquished'), ('57', 'Revoked'), ('80', 'Deceased')], max_length=255, null=True)),
                ('lic_type', models.CharField(blank=True, choices=[('SALE', 'TREC - Sales Agent'), ('BRK', 'TREC - Individual Broker'), ('BLLC', 'TREC - Limited Liability Corporation Broker'), ('BCRP', 'TREC - Corporation Broker'), ('6', 'TREC - Partnership Broker'), ('REB', 'TREC - Broker Organization Branch'), ('PRIN', 'TREC - Professional Inspector'), ('REIN', 'TREC - Real Estate Inspector'), ('APIN', 'TREC - Apprentice Inspector'), ('ILLC', 'TREC - Professional Inspector, LLC'), ('ICRP', 'TREC - Professional Inspector, Corporation'), ('ERWI', 'TREC - Easement and Right-of-Way, Individual'), ('ERWO', 'TREC - Easement and Right-of-Way, Business')], max_length=255, null=True)),
                ('lic_date_orig', models.DateField(blank=True, null=True)),
                ('lic_date_exp', models.DateField(blank=True, null=True)),
                ('trec_ed_status', models.CharField(blank=True, choices=[('0', 'No Non-elective CE Requirement'), ('1', 'Non-elective CE Requirements Outstanding'), ('2', 'Non-elective CE Requirements Met')], max_length=255, null=True)),
                ('trec_mce_status', models.CharField(blank=True, choices=[('0', 'No MCE Requirement'), ('1', 'MCE Requirements Outstanding'), ('2', 'MCE Requirements Met')], max_length=255, null=True)),
                ('source_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_gen.SourceListModel')),
            ],
        ),
    ]