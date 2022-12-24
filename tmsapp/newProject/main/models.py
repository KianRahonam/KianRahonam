from django.db import models

# Create your models here.
class Userdata(models.Model): # Creating a Table
    objects = None
    firstname = models.CharField(max_length=50,default="")
    lastname = models.CharField(max_length=50,default="")
    phoneNum = models.CharField(max_length=12,default="")
    emailId = models.EmailField(max_length=100,default="")
    password = models.CharField(max_length=100,default="Admin")

