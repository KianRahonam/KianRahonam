from django.shortcuts import render
from .models import UserManagement
# Create your views here.

def mainpage(req):
    return render(req,'index.html')

def adddata(req):
    if req.method == 'POST':
        firstName = req.POST['firstName']
        lastName = req.POST['lastName']
        emailId = req.POST['emailId']
        gender = req.POST['gender']
        age = req.POST['age']
        role = req.POST['role']
        un = UserManagement(firstName=firstName,lastName=lastName,emailId=emailId,gender=gender,age=age,role=role)
        un.save()
        return render(req, 'index.html', {'message': 'Data Added'})
    else:
        return render(req, 'index.html', {'message': 'Data not Added'})

def getdata(req):
    data = UserManagement.objects.all()
    return render(req,'viewdata.html',{'data':data})