from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        # Check if the 'completed' field is in the POST data
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('todo_list')
    else:
        # Render the form if needed (not necessary for the checkbox functionality)
        form = TodoForm(instance=todo)
        return render(request, 'todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_confirm_delete.html', {'todo': todo})