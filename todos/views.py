from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import date

# 'select' de tudo da tabela Todo
from .models import Todo

# ja identifica que a template a ser renderizada é a todo_list.html
class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "project", "description", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "project", "description", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finishedAt = date.today()
        todo.save()
        return redirect("todo_list")
        # buscar na base de dados a coluna pk que tenha o pk igual ao passado pela requisicao da view. apos encontrar, atualizar o campo finishedAt. no final, salvar na base de dados e fazer um redirect.
        