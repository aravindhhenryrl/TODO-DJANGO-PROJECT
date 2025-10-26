from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

from .models import *
from .forms import *  


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context ={'tasks':tasks,'form':form}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')  
    return render (request, 'aravi/home.html',context)

def UpadateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    context = {'form':form}
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')  


    return render (request, 'aravi/update_task.html',context)

def DeleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item':item}
    return render(request,'aravi/delete.html',context)