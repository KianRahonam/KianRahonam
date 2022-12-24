
import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .models import bookingForm,BranchOffice,LorryHire,LoadingSheet

def loginPage(request):
    return render(request, "loginPage.html")

def signup(request):
    return render(request, "signupPage.html")

def createUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # firstname = request.POST["firstname"]
        # lastname = request.POST["lastname"]
        User.objects.create_superuser(username=username, password=password)

        return render(request, "loginPage.html", {"message": username + " User Created Successfully"})
    else:
        return render(request, "signupPage.html")

def mainview(request):
    return render(request, "base.html",)


def newBranch(request):
    # BranchOffice.objects.all().delete()
    data=BranchOffice.objects.all()
    return render(request,"createBranch.html",{"data":data})

def createBranch(request):
    if request.method=="POST":
        branchName = request.POST["branchName"]
        branchAddress = request.POST["branchAddress"]
        branchCity = request.POST["branchCity"]
        branchState = request.POST["branchState"]
        contactNumber = request.POST["contactNumber"]
        emailId = request.POST["emailId"]
        ownerShip = request.POST["ownerShip"]
        status = request.POST["status"]
        branchOffice = BranchOffice(branchName=branchName,
                                    branchAddress=branchAddress,
                                    branchCity=branchCity,
                                    branchState=branchState,
                                    contactNumber=contactNumber,
                                    emailId=emailId,
                                    ownerShip=ownerShip,
                                    status=status
                                    )
        branchOffice.save()
        data = BranchOffice.objects.all()
        return render(request,"createBranch.html",{"data":data})

def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            return render(request, "base.html", {"username":user})
        else:
            return render(request, "loginPage.html", {"message": "User / Password is Wrong"})


def logoutUser(request):
    logout(request)
    return render(request, "loginPage.html")


def userManagement(request):
    users = User.objects.all()
    return render(request, "userManagement.html", {"data": users})


def deleteUser(request):
    if request.method == "POST":
        remveUser = request.POST["username"]
        User.objects.get(username=remveUser, is_superuser=True).delete()
        return render(request, "base.html", {"message": remveUser + " Deleted Successfully"})

def bookingPage(request):
    branch = BranchOffice.objects.all()
    return render(request, "bookingPage.html",{'branch':branch})


def createBooking(request):
    if request.method == "POST":
        lrNumber = len(bookingForm.objects.all())+20220000
        bookingDate = request.POST["bookingDate"]
        bookingBranch = request.POST["bookingBranch"]
        deliveryBranch = request.POST["deliveryBranch"]
        deliveryType = request.POST["deliveryType"]
        consignore = request.POST["consignore"]
        consignee = request.POST["consignee"]
        billingAddress = request.POST["billingAddress"]
        deliveryAddress = request.POST["deliveryAddress"]
        vehicleNumber = request.POST["vehicleNumber"]
        noa = request.POST["noa"]
        weight = request.POST["weight"]
        billingType = request.POST["billingType"]
        docNumber = request.POST["docNumber"]
        docDate = request.POST["docDate"]
        packType = request.POST["packType"]
        value = request.POST["value"]
        count = request.POST["noa"]
        invWeight = request.POST["invWeight"]
        remark = request.POST["remark"]
        loadType = request.POST["loadType"]
        mot = request.POST["mot"]
        newbooking = bookingForm(mot=mot,value=value,count=count,invWeight=invWeight,remark=remark,lrNumber=str(lrNumber), bookingDate=bookingDate,bookingBranch=bookingBranch,deliveryBranch=deliveryBranch,deliveryType=deliveryType,consignee=consignee,consignore=consignore,billingAddress=billingAddress,billingType=billingType,deliveryAddress=deliveryAddress,vehicleNumber=vehicleNumber,noa=noa,weight=weight,docNumber=docNumber,docDate=docDate,packType=packType,loadType=loadType)
        newbooking.save()
        message ="LR #: {} Created Successfully".format(lrNumber)
        return render(request, "bookingView.html",{"lrnumber":message})

def viewBooking(request):
    return render(request, "bookingView.html")

def viewDetials(request):
    if request.method=="POST":
        lrNumber = request.POST.get('lrNumber')
        if lrNumber!= None:
            data = bookingForm.objects.filter(lrNumber=lrNumber)
            return render(request,"bookingView.html",{"data":data})
        else:
            return render(request,"bookingView.html",{"message":"{} Is not in Record".format(lrNumber)})

def track(request):
    if request.method=="POST":
        lrNumber = request.POST.get('lrNumber')
        if lrNumber!= None:
            data = bookingForm.objects.filter(lrNumber=lrNumber)
            return render(request,"track.html",{"data":data})
        else:
            return render(request,"track.html",{"message":"{} Is not in Record".format(lrNumber)})


def bookingReport(request):
    data = bookingForm.objects.all()
    datetime.date.today()
    datetime.datetime.now()
    return render(request,"bookingReport.html",{"data":data,'reportDate':datetime.datetime.now()})

def bookingUpdatePage(request):
    return render(request,"bookingUpdate.html")

def lrData(request):
    if request.method=="POST":
        lrNumber = request.POST.get('lrNumber')
        if lrNumber!= None:
            data = bookingForm.objects.filter(lrNumber=lrNumber).values()
            check=data[0]["status"]
            if check!="Ready":
                return render(request,"bookingUpdate.html", {"message":"{0} Is {1}".format(lrNumber,check)})
            return render(request,"bookingUpdate.html", {"data":data},)
        else:
            return render(request,"bookingUpdate.html",{"message":"{} Is not in Record".format(lrNumber)})

def mainPage(request):
    return render(request,"mainPage.html")

def lorryhirePage(request):
    data = LorryHire.objects.all()
    return render(request,'lorryhire.html',{'data':data})

def lorryHire(request):
    if request.method == "POST":
        tripNumber = len(LorryHire.objects.all())+1
        vehiclenumber = str(request.POST['vehiclenumber']).upper()
        vehicletype = request.POST['vehicleType']
        capacityWeight = request.POST['capacityWeight']
        driverName = request.POST['driverName']
        driverNumber = request.POST['driverNumber']
        hireAmount = request.POST['hireAmount']
        vendorName = request.POST['vendorName']
        status = 'Pending for Approval'
        check = LorryHire.objects.filter(vehiclenumber=vehiclenumber).filter(status='Pending for Approval').count()
        print(check)
        if check <1:
            readyLorry = LorryHire(tripNumber=tripNumber, vehiclenumber=vehiclenumber,vehicletype=vehicletype,capacityWeight=capacityWeight,driverName=driverName,driverNumber=driverNumber,hireAmount=hireAmount,vendorName=vendorName,status=status)
            readyLorry.save()
            message = 'Lorry Hired : {}'.format(vehiclenumber)
            return render(request,'lorryhire.html',{'message':message})
        else:
            message = 'Awaiting For Loading : {}'.format(vehiclenumber)
            return render(request,'lorryhire.html',{'message':message})

# @loginUser
def approve(request,id):
    udata = LorryHire.objects.get(pk=id)
    udata.status = 'Approved'
    udata.save()
    vhnumber = udata.vehiclenumber
    data = LorryHire.objects.all()
    return render(request,'lorryhire.html',{'data':data,'message':'VH Approved for : {}'.format(vhnumber)})

def reject(request,id):
    data = LorryHire.objects.get(pk=id).delete()
    return render(request,'lorryhire.html',{'data':data,'message':'VH Rejected'})

def clearall(request):
    data = LorryHire.objects.all().delete()
    return render(request,'lorryhire.html',{'data':data})

def loadingPage(request):
    lh = LorryHire.objects.filter(status='Approved')
    bo = BranchOffice.objects.all()
    ls = LoadingSheet.objects.all()
    return render(request, 'loadingPage.html', {'data': lh, 'branch': bo,'ls':ls})


def load_consignment(request):
    lh = LorryHire.objects.filter(status='Approved')
    bo = BranchOffice.objects.all()
    ls = LoadingSheet.objects.all()
    lrNumbers = []

    if request.method == 'POST':
        tsNumber = request.POST['tsNumber']
        lrNumber = request.POST.get('lrNumber')
        vehiclenumber = request.POST['vehicleNumber']
        lr = bookingForm.objects.filter(lrNumber=lrNumber).values
        weight = 100
        print(weight)
        no_articals = 10
        print(no_articals)
        vendorName ='self'
        loadingBranch = "Bangalore"
        deliveryBranch = "Chennai"
        status = 'Loaded'
        ls_data = LoadingSheet(lsNumber=tsNumber,lrNumber=lrNumber,vehiclenumber=vehiclenumber,weight=weight,no_articals=no_articals,vendorName=vendorName,loadingBranch=loadingBranch,deliveryBranch=deliveryBranch,status=status)
        ls_data.save_base()
        lsdata = LoadingSheet.objects.filter(tsNumber=tsNumber)
        return render(request,'loadingPage.html',{'data':lh,'branch':bo,'ls':ls,'lsdata':lsdata})


def lrDataUpdate(request):
    lrNumber = request.POST['lrNumber']
    udata = bookingForm.objects.get(lrNumber=lrNumber)
    print(lrNumber)
    bookingBranch = request.POST['bookingBranch']
    deliveryBranch = request.POST['deliveryBranch']
    udata.bookingBranch = request.POST['bookingBranch']
    udata.deliveryBranch = request.POST['deliveryBranch']
    udata.update()
    return render(request,"bookingUpdate.html",{"message":"{} Update".format(lrNumber)})

def uploadPod(request):
    return render(request,'upload.html')

from .models import producPic

def uploadFile(request):
    if request.method == 'POST':
        file = request.POST['file']
        data = producPic(image=file)
        data.save_base()
        return render(request,'upload.html')