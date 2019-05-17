# Generated by Django 2.2.1 on 2019-05-15 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_gen', '0008_auto_20190515_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='lic_type',
            field=models.CharField(choices=[('N/A', 'Not Available'), ('SALE', 'TREC - Sales Agent'), ('BRK', 'TREC - Individual Broker'), ('BLLC', 'TREC - Limited Liability Corporation Broker'), ('BCRP', 'TREC - Corporation Broker'), ('6', 'TREC - Partnership Broker'), ('REB', 'TREC - Broker Organization Branch'), ('PRIN', 'TREC - Professional Inspector'), ('REIN', 'TREC - Real Estate Inspector'), ('APIN', 'TREC - Apprentice Inspector'), ('ILLC', 'TREC - Professional Inspector, LLC'), ('ICRP', 'TREC - Professional Inspector, Corporation'), ('ERWI', 'TREC - Easement and Right-of-Way, Individual'), ('ERWO', 'TREC - Easement and Right-of-Way, Business'), ('APCR', 'TALCB - Certified Residential Appraiser'), ('APGN', 'TALCB - Certified General Appraiser'), ('APOS', 'TALCB - Temporary Out of State Appraiser'), ('APPV', 'TALCB - Provisional Licensed Appraiser'), ('APSC', 'TALCB - Licensed Residential Appraiser'), ('APTR', 'TALCB - Appraiser Trainee'), ('BR', 'OREC - Broker'), ('SA', 'OREC - Sales Associate'), ('PS', 'OREC - Provisional Sales Associate')], default='N/A', max_length=255),
        ),
    ]