from django.db import models

# Create your models here.

class UserAccount(models.Model):
    objects = None
    emailID = models.EmailField(primary_key=True,max_length=50)
    firstName = models.CharField(default="",max_length=25)
    lastName = models.CharField(default="", max_length=25)
    phoneNumber = models.CharField(default="0000000000",max_length=12)
    status = models.CharField(default="Pending",max_length=20)

    def __str__(self):
        return self.emailID


