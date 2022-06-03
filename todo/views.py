from django.shortcuts import redirect, render

from django.http import HttpResponse

from .models import Task

from .forms import TaskForm

# CRUD-list

def task_list(request):
    tasks = Task.objects.all().order_by('-due_date')
    context = {
        'tasks':tasks
    }
    print(context)
    return render(request, 'todo/task_list.html', context)

def task_create(request):
    if (request.method == 'POST'):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_task_list')
    else:
        form = TaskForm()
    
    context = {
        'form': form
    }
    print(context)
    return render(request, 'todo/task_create.html', context)

def task_details(request, id):
   # return HttpResponse(f'Détails d\'une tâche id : {id}')
    task = Task.objects.get(id=id)
    context = {
        'task': task
    }
    return render(request, 'todo/task_details.html', context)

def task_update(request, id):
    return HttpResponse(f'Update d\'une tâche : {id}')

def task_delete(request, id):
    # return HttpResponse(f'Delete d\'une tâche : {id}')
    task = Task.objects.get(id=id)
    context = {
        'task': task
    }
    task.delete()
    return render(request, 'todo/task_delete.html', context)