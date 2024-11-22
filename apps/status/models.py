from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class CategoriaStatus(models.Model):
    nome= models.TextField(blank=True,
                           null=True)
    
class Status(models.Model):
    nome = models.TextField(blank=True)
    categoria = models.ForeignKey(CategoriaStatus, on_delete=models.SET_NULL, null=True)
    texto = CKEditor5Field(
        'descricao', config_name='extends', blank=True, null=True
    )
    
    
    
    def __str__(self):
        return self.nome
