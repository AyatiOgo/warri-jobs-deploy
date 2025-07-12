from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class RegularUSer(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.email
