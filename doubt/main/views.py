from django.shortcuts import render
from .models import UserAccount

# Create your views here.

from .forms import signUpform
def index(request):
    form = signUpform
    data = UserAccount.objects.all()
    return render(request,"index.html",{'form':form,'data':data})

def createUser(request):
    if request.method == "POST":
        form = signUpform
        form = signUpform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"index.html",{'form':form,"message":'User Created'})
        else:
            return render(request,"index.html",{"message":'Please try Again !!!'})

def search(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        data = UserAccount.objects.all().filter(firstName=firstName)
        return render(request,"index.html",{'data':data})




