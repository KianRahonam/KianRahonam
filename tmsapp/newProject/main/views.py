from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request,'mainPage.html')

def loginPage(request):
    return render(request,'login.html')

def authuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST['password']
        from .models import Userdata
        data = Userdata.objects.get(emailId=username)
        print(type(data))
        return render(request,'mainPage.html')

def sighup(request):
    return render(request,'reg.html')

def adduser(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phoneNum = request.POST['lastname']
        emialid = request.POST['emailid']
        from .models import Userdata
        data = Userdata(firstname=firstname,lastname=lastname,phoneNum=phoneNum,emailId=emialid)
        data.save()
        fdata = Userdata.objects.all()
        return render(request,'reg.html',{'message':'{} {} Created !'.format(firstname,lastname),'data':fdata})
