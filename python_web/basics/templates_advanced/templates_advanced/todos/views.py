from django.shortcuts import redirect, render
from templates_advanced.todos.forms import TodoForm
from templates_advanced.todos.models import Todo

# Create your views here.


def list_todos(request):
    context = {
        'todos': Todo.objects.all(),
        'page_name': 'list_todos'
    }
    return render(request, 'todos/list_todos.html', context)


def create_todo(request):
    form = TodoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list todos')
    context = {
        'form': form,
        'page_name': 'create_todo'

    }
    return render(request, 'todos/create_todo.html', context)
