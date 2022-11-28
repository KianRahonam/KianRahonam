from django.db import models


class studentData(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
# Create your models here.
