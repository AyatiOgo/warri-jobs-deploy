# Generated by Django 5.2.1 on 2025-06-06 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1500)),
                ('company_name', models.CharField(max_length=200)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('job_type', models.CharField(choices=[('partime', 'Partime'), ('fulltime', 'Fulltime')], max_length=50)),
                ('work_location', models.CharField(choices=[('remote', 'Remote'), ('hybrid', 'Hybrid'), ('on-site', 'On-site')], max_length=50)),
                ('categories', models.CharField(choices=[('Customer Service', 'Customer Service'), ('Operations', 'Operations'), ('Retail', 'Retail'), ('Marketing', 'Marketing'), ('Administrative', 'Administrative'), ('Creative / Digital', 'Creative / Digital')], max_length=50)),
                ('core_tasks', models.TextField(max_length=1500)),
                ('requirements', models.TextField(max_length=1500)),
                ('nice_to_have', models.TextField(blank=True, max_length=1500, null=True)),
                ('benefits', models.TextField(blank=True, max_length=1500, null=True)),
                ('contact_info', models.CharField(max_length=1500)),
            ],
        ),
    ]
