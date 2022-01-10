from django.shortcuts import redirect, render, HttpResponse
from .forms import TodoListForm
from .models import *

def index(request):
    form = TodoListForm()

    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    todos = TodoList.objects.all()
    
    context = {
        "todo_form": form,
        "todos": todos,
        
    }
    return render(request, "todolist/index.html", context)

def completed(request, pk):
    todo = TodoList.objects.get(id=pk)
    if todo.completed == True:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('/')

def important(request, pk):
    todo = TodoList.objects.get(id=pk)
    if todo.important == True:
        todo.important = False
    else:
        todo.important = True
    todo.save()
    return redirect('/')

def update(request, pk):
    todo = TodoList.objects.get(id=pk)

    form = TodoListForm(instance=todo)

    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "todoEditForm": form
    }
    return render(request, "todolist/update.html", context)

# def complete(request, pk):
#     todo = TodoList.objects.get(id=pk)
#     if todo.completed == True:
#         todo.completed = True
#     else:
#         todo.completed = False
#     return redirect("index")

def delete(request, pk):
    todo = TodoList.objects.get(id=pk)
    todo.delete()
    return redirect("index")