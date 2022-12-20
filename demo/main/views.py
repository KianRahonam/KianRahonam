from django.shortcuts import render
from .models import Userdata

def loginPage(request):
    return render(request,'index.html')

def loginUser(request):
    if request.method == 'POST':
        user = request.POST['username']
        pasc = request.POST['password']
        return render(request,'mainPage.html',{'user':user,'pasc':pasc})

def adduserPage(request):
    return render(request,'adduser.html')

def adduser(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        emailId = request.POST['emailId']
        phoneNumber = request.POST["phoneNumber"]
        status = request.POST['status']
        print(firstname,lastname,emailId,phoneNumber,status)
        user = Userdata(firstname=firstname,lastname=lastname,emailId=emailId,phoneNumber=phoneNumber,status=status).save()
        data = Userdata.objects.all()
        return render(request,'viewdata.html',{'message':'User Created !','data':data})

def FatchDate(request):
    data = Userdata.objects.all() # Fatching the data JSON format
    return render(request,"viewdata.html",{'data':data})

    
def FatchDate(request):
    data = Userdata.objects.all() # Fatching the data JSON format
    return render(request,"viewdata.html",{'data':data})

def searchPage(request):
    return render(request,'searchdata.html')

def searchdata(request):
    if request.method == "POST":
        useremailid = request.POST['emailId']
        data = Userdata.objects.filter(emailId=useremailid)
        # d=len(data)
        return render(request,"searchdata.html",{'keydata':data})


from .forms import ImageForm

def uploadPage(request):
    form = ImageForm(request.POST, request.FILES)
    return render(request, 'uploadfile.html', {'form': form})

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'uploadfile.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'uploadfile.html', {'form': form})