from django.shortcuts import render,HttpResponse
from models import User,Family
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return HttpResponse("Login successful.")
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
        family = Family.objects.create(family_name = "Muller")
        user = User.objects.create_user(username=username,password=password,
                                        #todo
                                        gender=True,age=20,family_name=family)
        user.save()
        return HttpResponse("You registered successful!")
    else:
        return render(request,'user-register.html')