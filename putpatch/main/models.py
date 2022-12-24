from django.db import models

# Create your models here.

class IssueTickets(models.Model):
    ticketNumber = models.IntegerField(primary_key=True)
    createdBy = models.CharField(max_length=25,default="")
    issueDetial = models.CharField(max_length=150,default="")
    status = models.CharField(max_length=20,default="")
    assignedTo = models.CharField(max_length=25,default="admin")
