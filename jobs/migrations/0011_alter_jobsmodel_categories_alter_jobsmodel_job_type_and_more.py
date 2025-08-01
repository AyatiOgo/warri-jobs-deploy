# Generated by Django 5.2.1 on 2025-07-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_alter_jobsmodel_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsmodel',
            name='categories',
            field=models.CharField(choices=[('Operations', 'Operations'), ('Administrative', 'Administrative'), ('Creative / Digital', 'Creative / Digital'), ('Customer Service', 'Customer Service'), ('Retail', 'Retail'), ('Marketing', 'Marketing')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobsmodel',
            name='job_type',
            field=models.CharField(choices=[('partime', 'Partime'), ('fulltime', 'Fulltime')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobsmodel',
            name='work_location',
            field=models.CharField(choices=[('hybrid', 'Hybrid'), ('remote', 'Remote'), ('on-site', 'On-site')], max_length=50),
        ),
    ]
