from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegistrationView, name='register'),
    path('login/', userLoginView, name='login'),
    path('logout/', userLogoutView, name='logout'),
    path('add_saved/<int:id>', add_saved, name='add_saved'),
    path('saved/', saved_jobs, name='saved'),
]