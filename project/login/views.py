from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    return render(request,'index.html')

def signupPage(request):
    return render(request,'signup.html')

def loginPage(request):
    return render(request,'login.html')

def createUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =User(username=username,password=password)
        user.save()
        return render(request,'login.html',{'message':'{} User Created'.format(username)})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user.is_valid():
            return render(request,'main.html',{'message':'Welcome {}'.format(username)})
        else:
            return render(request,'login.html',{'message':'Your Not Allowed {}'.format(username)})

# Create your views here.
