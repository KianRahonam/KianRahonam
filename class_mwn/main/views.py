from django.shortcuts import render
from .models import UserManagement

# Create your views here.


def main(request):
    return render(request,'index.html')

def adduserPage(request):
    return render(request,'index.html')

def adduser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        phone = request.POST['phone']

        um = UserManagement(username=username,password=password,firstName=firstname,lastName=lastname,gender=gender,phone=phone)
        um.save()
        message = {"msg":"{} Created Successfully !".format(username)}
        return render(request,'index.html',message)


def updateUser(request):
    return render(request,'updateUser.html')

def updateUserData(request):
    if request.method == "POST":
        emailid = request.POST['emailid']
        un = UserManagement.objects.filter(username=emailid)
        return render(request,'updateUser.html',{"data":un})

def fatchUser(request,pk):
    if request.method == 'POST':
        pk = request.POST.get("username")
        um = UserManagement.objects.filter(username=pk)
        return render(request,'updateUser.html',{'data':um})


