from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from autoslug import AutoSlugField
from accounts.models import RegularUSer
# Create your models here.

class JobsModel(models.Model):

    JOB_TYPE_CHOICES= {
        ('fulltime', 'Fulltime'),
        ('partime', 'Partime'),
    }

    WORK_LOCATION_CHOICES= {
        ('on-site', 'On-site'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
    }

    CATEGORY_CHOICES= {
        ('Customer Service', 'Customer Service'),
        ('Operations', 'Operations'),
        ('Marketing', 'Marketing'),
        ('Retail', 'Retail'),
        ('Administrative', 'Administrative'),
        ('Creative / Digital', 'Creative / Digital'),
    }


    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    slug = AutoSlugField(populate_from='title', unique=True, blank=True, null=True, always_update=True)
    company_name = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    job_type = models.CharField( max_length=50, choices=JOB_TYPE_CHOICES )
    work_location = models.CharField( max_length=50, choices=WORK_LOCATION_CHOICES)
    categories = models.CharField( max_length=50,  choices=CATEGORY_CHOICES)
    core_tasks = models.TextField(max_length=1500)
    requirements = models.TextField(max_length=1500)
    nice_to_have = models.TextField(max_length=1500, null=True, blank=True)
    benefits = models.TextField(max_length=1500, null=True, blank=True)
    contact_info = models.CharField(max_length=1500)
    saved = models.ManyToManyField(RegularUSer, related_name='saved', blank=True )
    job_link = models.URLField(default="#")

    def __str__(self):
        return self.title
