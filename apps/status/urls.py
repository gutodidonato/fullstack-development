from django.urls import path, include
from ..status.views import index,send_email


urlpatterns = [
    path('', index, name='index'),
    path('send_email/', send_email, name='send_email')
    #path('contato', contato, name='contato')
] 
