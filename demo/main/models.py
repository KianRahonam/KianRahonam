from django.db import models


class Userdata(models.Model):
    object=None
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    emailId = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

# Create your models here.
