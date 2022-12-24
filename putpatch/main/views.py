from django.shortcuts import render
from .forms import ticketForm
# Create your views here.

def index(request):
    form = ticketForm
    return render(request,"index.html",{"form":form})

def createTicket(request):
    if request.method == "POST":
        form = ticketForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"index.html",{'message':"Ticket Created !"})

def updatedata(request,id):
    if request.method == "PUT":
        form = ticketForm(request.PUT)
        if form.is_valid():
            form.save()
            return render(request,"index.html",{'message':"Ticket Updated !"})