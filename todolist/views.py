from django.shortcuts import render,HttpResponse,HttpResponseRedirect
# from models import User,Family
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.admin.views.decorators import staff_member_required
from models import Todo
from accounts.models import User

def family_calender(request):
    tasks = Todo.objects.filter(family=request.user.family_name)
    return render(request,'all-todo-list.html',
                  {'tasks':tasks})

def create_new_todo(request):
    tasks = Todo.objects.filter(user=request.user)
    if request.method == 'GET':
        users = User.objects.filter(family_name=request.user.family_name)
        return render(request,'create-new-todo.html',
                      {'users':users,'tasks':tasks})
    else:
        task = request.POST['task']
        deadline = request.POST['deadline']
        user = User.objects.get(id=request.POST['towho'])
        task = Todo.objects.create(task=task,deadline=deadline,
                                   user=user,family=request.user.family_name)
        task.save()
        return HttpResponse('Save successfully!')

def my_todo(request):
    tasks = Todo.objects.filter(user=request.user)
    return render(request,'all-todo-list.html',
                  {'tasks':tasks})