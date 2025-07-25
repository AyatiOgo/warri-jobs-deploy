# Generated by Django 5.2.1 on 2025-06-15 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_jobsmodel_categories_alter_jobsmodel_job_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsmodel',
            name='categories',
            field=models.CharField(choices=[('Administrative', 'Administrative'), ('Operations', 'Operations'), ('Retail', 'Retail'), ('Customer Service', 'Customer Service'), ('Marketing', 'Marketing'), ('Creative / Digital', 'Creative / Digital')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobsmodel',
            name='job_type',
            field=models.CharField(choices=[('fulltime', 'Fulltime'), ('partime', 'Partime')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobsmodel',
            name='work_location',
            field=models.CharField(choices=[('remote', 'Remote'), ('hybrid', 'Hybrid'), ('on-site', 'On-site')], max_length=50),
        ),
    ]
