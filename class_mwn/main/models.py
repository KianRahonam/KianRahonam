from django.db import models

# Create your models here.

class UserManagement(models.Model):
    objects = None
    username = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
