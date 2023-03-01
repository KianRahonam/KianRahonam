from django.db import models

# Create your models here.

class UserManagement(models.Model):
    objects = None
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    emailId = models.EmailField(max_length=100)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    role = models.CharField(max_length=25)

