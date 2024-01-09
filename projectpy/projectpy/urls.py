# projectpy/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', include('lista_tarefas.urls')),
    path('', include('lista_tarefas.urls')),  # Adicione esta linha para a raiz
]
