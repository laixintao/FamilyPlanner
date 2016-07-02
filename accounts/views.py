# -*- coding: utf-8 -*-

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from models import User,Family
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.admin.views.decorators import staff_member_required

def login(request):
    haserrror = False
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request,user)
                return HttpResponseRedirect("/user")
            else:
                return render(request,'user-login.html',
                              {'haserror':True,
                               'message':"User is not active."})
        else:
            return render(request,'user-login.html',
                              {'haserror':True,
                               'message':"Wrong username or password."})
    else:
        return render(request, 'user-login.html',{
            'haserror':False
        })

def register(request):
    if request.method == 'POST':
        haserror = False
        try:
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
                                            gender=gender,age=age,family_name=family,
                                            is_staff=True,role=True)
            user.save()
            return HttpResponseRedirect('/login/')
        except:
            haserror = True
            return render(request,'user-register.html',
                          {'message':'Sorry, the username is already using or you missed something,try it again!',
                           'haserror':haserror})
    else:
        return render(request,'user-register.html',
                      {'haserror':False})

def index(request):
    user = request.user
    print user.username
    return render(request,"profile.html",
                  {'user':user})

@staff_member_required
def add_memnbers(request):
    if request.method == 'GET':
        return render(request,"addMember.html")
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
            family = request.user.family_name
            print username,password,family
            age = request.POST['age']
            gender = True
            if request.POST['gender'] == "true":
                pass
            else:
                gender = False
            role = False
            if request.POST['role'] == "true":
                gender = True
            else:
                gender = False
            user = User.objects.create_user(username=username,password=password,age=age,
                                       family_name=family,gender=gender,role=role)
            print user.password
            user.save()
            return HttpResponseRedirect('/family-calender/')
        except:
            haserror = True
            return render(request,'user-register.html',
                          {'message':'Try another username!',
                           'haserror':haserror})