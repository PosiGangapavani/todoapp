from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.shortcuts import redirect,get_object_or_404

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_complete(request,pk):
    mark = get_object_or_404(Task,pk=pk)
    mark.is_completed = True
    mark.save()
    return redirect('home')

def mark_as_undone(request,pk):
    mark = get_object_or_404(Task,pk=pk)
    mark.is_completed = False
    mark.save()
    return redirect('home')

def edit_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task  = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task':get_task,
        }
        return render(request,'edit_task.html',context)
def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')