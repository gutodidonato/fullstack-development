from django.urls import path, include
from ..status.views import index, projeto


urlpatterns = [
    path('', index, name='index'),
    path('projeto', projeto, name='projeto')
    #path('contato', contato, name='contato')
] 
