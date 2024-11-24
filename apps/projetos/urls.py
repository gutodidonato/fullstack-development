from django.urls import path, include
from ..projetos.views import projeto, listagem_projeto


urlpatterns = [
    path('projetos/', listagem_projeto, name='listagem_projeto'),
    path('projeto/<int:projeto_id>', projeto, name='projeto')
] 
