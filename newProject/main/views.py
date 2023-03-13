from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'navbar.html',{'site':'home',"home":'active'})

def addpage(req):
    return render(req,'navbar.html',{'site':'createuser',"add":'active'})

def updatePage(req):
    return render(req,'navbar.html',{"site":'updatepage',"update":'active',"un":""})

def deletePage(req):
    return render(req,'navbar.html',{'site':'deletepage',"delete":'active'})

def viewPage(req):
    from .models import UserManagement
    data = UserManagement.objects.all()
    return render(req,'navbar.html',{"site":'view',"view":'active','data':data})

def createUser(req):
    from .models import UserManagement
    if req.method == 'POST':
        username = req.POST['un']
        password = req.POST['pw']
        firstname = req.POST['fn']
        lastname = req.POST['ln']
        email = req.POST['em']
        phone = req.POST['ph']
        gender = req.POST['gn']
        role = req.POST['rl']
        status = 'Pending'
        um = UserManagement(id=username,
                            ps=password,
                            firstname=firstname,
                            lastname=lastname,
                            email=email,
                            phone=phone,
                            gender=gender,
                            role=role,
                            status=status
                            )
        um.save()
        return render(req, 'navbar.html', {"site": 'createuser',
                                           "view": 'active',
                                           'msg':'{} User Create !'.format(username)})

def fatchUser(req):
    from .models import UserManagement
    if req.method == 'POST':
        id = req.POST['un']
        um = UserManagement.objects.get(id=id)
        print(um.firstname)
        return render(req, 'navbar.html', {"site": 'updatepage', "update": 'active','data':um})
#
def updateUser(req):
    from .models import UserManagement
    if req.method == 'POST':
        username = req.POST['un']
        password = req.POST.get('ps')
        firstname = req.POST.get('fn')
        lastname = req.POST.get('ln')
        email = req.POST.get('em')
        phone = req.POST.get('ph')
        gender = req.POST.get('gn')
        role = req.POST.get('rl')
        status = 'Updated'

        um = UserManagement(id=username,ps=password,firstname=firstname,lastname=lastname,email=email,phone=phone,gender=gender,role=role,status=status)
        um.save()

    return render(req, 'navbar.html', {"site": 'updatepage', "update": 'active'})

