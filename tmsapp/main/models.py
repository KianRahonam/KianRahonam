import datetime
import os.path

from django.db import models
import datetime
# Create your models here.

class bookingForm(models.Model):
    objects = None
    lrNumber = models.CharField(max_length=10,null=True)
    mot = models.CharField(max_length=20,default="Road",blank=True)
    status = models.CharField(default="Ready",max_length=10,blank=True)
    bookingDate = models.DateField(default=datetime.datetime.today())
    bookingBranch = models.CharField(max_length=50,null=True)
    deliveryBranch = models.CharField(max_length=50,null=True)
    deliveryType = models.CharField(max_length=50,null=True)
    consignore = models.CharField(max_length=50,null=True)
    consignee = models.CharField(max_length=50,null=True)
    fgstn = models.CharField(max_length=13,default=29000000000)
    ngstn = models.CharField(max_length=13,default=29000000000)
    billingAddress = models.CharField(max_length=100,default="")
    deliveryAddress = models.CharField(max_length=100,default="")
    vehicleNumber = models.CharField(max_length=10,default="")
    freightAmount = models.FloatField(default=0.0)
    hamaliCharges = models.FloatField(default=0.0)
    noa = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    billingType = models.CharField(max_length=20,default="")
    docNumber = models.CharField(max_length=50,default="")
    docDate = models.CharField(max_length=50, default="")
    packType = models.CharField(max_length=50,default="")
    value = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    invWeight = models.IntegerField(default=0)
    remark = models.CharField(max_length=150,default="")
    loadType = models.CharField(max_length=50,default="FTL")
    loadingSheet = models.CharField(max_length=10,null=True)
    pod_link = models.FilePathField(path='/pods',default='')
    

    def __str__(self):
        return self.lrNumber


class BranchOffice(models.Model):
    objects = None
    branchName = models.CharField(max_length=50,null=True)
    branchAddress = models.CharField(max_length=100,null=True)
    branchCity = models.CharField(max_length=20,null=True)
    branchState = models.CharField(max_length=20,null=True)
    contactNumber = models.CharField(max_length=12,null=True)
    emailId = models.EmailField(max_length=50,null=True)
    ownerShip = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=20,null=True)
    lrnumberSl = models.CharField(max_length=8,default=20220000,null=True)


    def __str__(self):
        return self.branchName


class LorryHire(models.Model):
    objects = None
    tripNumber = models.CharField(max_length=10,default="")
    tripDate = models.DateField(auto_now=True)
    vehiclenumber = models.CharField(max_length=10)
    vehicletype = models.CharField(max_length=20)
    capacityWeight = models.IntegerField(default=0)
    loadWeight = models.IntegerField(default=0)
    driverName = models.CharField(max_length=20,default="")
    driverNumber = models.CharField(default="", max_length=12)
    hireAmount = models.FloatField(default=0.0)
    vendorName = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.tripNumber


class LoadingSheet(models.Model):
    objects = None
    lsNumber = models.CharField(max_length=10,default="")
    lrNumber = models.CharField(max_length=10,default="")
    primery_key = models.CharField(max_length=12,auto_created=str(lsNumber)+str(lrNumber),primary_key=True)
    vehiclenumber = models.CharField(max_length=10)
    weight = models.FloatField(default=0)
    no_articals = models.IntegerField(default=0)
    vendorName = models.CharField(max_length=50)
    loadingBranch = models.CharField(max_length=50)
    deliveryBranch = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return str(self.lrNumber) + str(self.lsNumber)

class producPic(models.Model):
    image = models.ImageField(null=True,blank=True)