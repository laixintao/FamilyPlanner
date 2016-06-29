from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from models import User,Family
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request,user)
                return HttpResponseRedirect("/user")
            else:
                return HttpResponse("User is not active.")
        else:
            return HttpResponse("Wrong username or password.")
    else:
        return render(request, 'user-login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        family = Family.objects.create(family_name = request.POST['familyname'])
        age = request.POST['age']
        gender = True
        if request.POST['gender'] == "true":
            pass
        else:
            gender = False
        user = User.objects.create_user(username=username,password=password,
                                        gender=gender,age=age,family_name=family)
        user.save()
        return HttpResponse("You registered successful!")
    else:
        return render(request,'user-register.html')

def index(request):
    user = request.user
    print user.username
    return render(request,"profile.html",
                  {'user':user})