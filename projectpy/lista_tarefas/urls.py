# lista_tarefas/urls.py
from django.urls import path
from .views import listar_tarefas, adicionar_tarefa, editar_tarefa, excluir_tarefa, home

urlpatterns = [
    path('', home, name='home'),  # Adicione esta linha para a raiz
    path('listar/', listar_tarefas, name='listar_tarefas'),
    path('adicionar/', adicionar_tarefa, name='adicionar_tarefa'),
    path('editar/<int:pk>/', editar_tarefa, name='editar_tarefa'),
    path('excluir/<int:pk>/', excluir_tarefa, name='excluir_tarefa'),
]
