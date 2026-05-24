from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo
from .froms import TodoForm


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/list.html", {"todos": todos})


def todo_delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        print(todo)
        todo.delete()
    except:
        print("無此ID")

    return redirect("todo-list")


def todo_create(request):
    return render(request, "todos/create.html", {"form": TodoForm()})
