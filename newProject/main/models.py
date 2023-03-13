from django.db import models

# Create your models here.

class UserManagement(models.Model):
    objects = None
    id = models.CharField(max_length=50, primary_key=True)
    ps = models.CharField(max_length=20, null=True)
    firstname = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    gender = models.CharField(max_length=5, null=True)
    phone = models.CharField(max_length=12, null=True)
    role = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=10)
