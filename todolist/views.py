from django.shortcuts import render,HttpResponse,HttpResponseRedirect
# from models import User,Family
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.admin.views.decorators import staff_member_required
from models import Todo

def family_calender(request):
    tasks = Todo.objects.filter(family=request.user.family_name)
    return render(request,'all-todo-list.html',
                  {'tasks':tasks})

def create_new_todo(request):
    if request.method == 'GET':
        return render(request,'create-new-todo.html')
    else:
        task = request.POST['task']
        deadline = request.POST['deadline']
        task = Todo.objects.create(task=task,deadline=deadline,
                                   user=request.user,family=request.user.family_name)
        task.save()
        return HttpResponse('Save successfully!')

def my_todo(request):
    tasks = Todo.objects.filter(user=request.user)
    return render(request,'all-todo-list.html',
                  {'tasks':tasks})