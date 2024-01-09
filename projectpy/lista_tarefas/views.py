# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa

# lista_tarefas/views.py
from django.shortcuts import redirect

def home(request):
    return redirect('listar_tarefas')


def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'lista_tarefas/listar_tarefas.html', {'tarefas': tarefas})

def adicionar_tarefa(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(descricao=descricao)
        return redirect('listar_tarefas')
    return render(request, 'lista_tarefas/adicionar_tarefa.html')

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        tarefa.descricao = descricao
        tarefa.save()
        return redirect('listar_tarefas')

    return render(request, 'lista_tarefas/editar_tarefa.html', {'tarefa': tarefa})

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('listar_tarefas')
