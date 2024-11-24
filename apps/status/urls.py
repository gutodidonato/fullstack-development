from django.urls import path, include
from ..status.views import index


urlpatterns = [
    path('', index, name='index')
    #path('contato', contato, name='contato')
] 
