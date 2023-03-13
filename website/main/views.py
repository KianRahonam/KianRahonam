from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req,'loginPage.html')

def loginPage(req):
    return render(req,'loginPage.html')

def loginUser(req):
    return render(req,'loginPage.html')

def signupPage(req):
    return render(req,'signupPage.html')

def adduser(req):
    return render(req,'loginPage.html')
