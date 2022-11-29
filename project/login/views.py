from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    return render(request,'index.html')

def signupPage(request):
    return render(request,'signup.html')

def createUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST.get('repassword')
      
        if re_password == password:
            user =User(username=username,password=password)
            user.save()
            return render(request,'login.html',{'message':'{} User Created'.format(username)})
        else:
            return render(request,'signup.html',{'message':"Password not matching"})

def loginPage(request):
    return render(request,'login.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            return render(request,'main.html',{'message':'Welcome {}'.format(username)})
        else:
            return render(request,'login.html',{'message':'Your Not Allowed {}'.format(username)})


from .models import studentData 
def studentCreation(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        s=studentData(firstname=firstname,lastname=lastname)
        s.save()


# Create your views here.
