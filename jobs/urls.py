from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', homeview, name='home'),
    path('job/<str:slug>', jobDetailView, name='job-detail'),
    path('search/', searchView, name='search'),
    path('jobslist/', joblist, name='jobslist'),
    path('add-job/', add_job_view, name='add-job'),
]