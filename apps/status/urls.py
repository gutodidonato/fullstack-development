from django.urls import path, include
from ..status.views import index, projeto, listagem_projeto


urlpatterns = [
    path('', index, name='index'),
    path('projetos/', listagem_projeto, name='listagem_projeto'),
    path('projeto/', projeto, name='projeto'),
    #path('contato', contato, name='contato')
] 
