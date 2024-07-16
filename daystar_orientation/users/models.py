from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['name', 'email', 'admission_number', 'course', 'phone_number']
