from django.shortcuts import render

# Create your views here.

def mainPage(req):
    user = input("User Name")
    return render(req,'index.html',{'user':user})

