from django.db import models
from ..skills.models import Skill
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

class CategoriaProjeto(models.Model):
    nome = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
class Projeto(models.Model):
    categoria_projeto = models.ForeignKey(
        CategoriaProjeto, on_delete=models.SET_NULL, related_name='projetos', null=True, blank=True
    )
    skills = models.ManyToManyField(
        Skill, related_name='projeto', blank=True
    )
    
    
    nome = models.CharField(max_length=255, blank=True)
    resumo = models.TextField(blank=True)
    imagem_inicio = models.ImageField(
        upload_to='projeto/start', blank=True, null=True
    )
    texto = CKEditor5Field(
        'descricao', config_name='extends'
    )
    
    link_github= models.CharField(max_length=255, blank=True)
    link_demo= models.CharField(max_length=255, blank=True)
    
    data_inicio = models.TextField(blank=True)
    data_fim = models.TextField(blank=True)
    cliente = models.TextField(blank=True)
    categoria = models.TextField(blank=True)
    
    
    imagem_galeria_1 = models.ImageField(
        upload_to='projeto/imagem_galeria', blank=True
    )
    imagem_galeria_2 = models.ImageField(
        upload_to='projeto/imagem_galeria', blank=True
    )
    imagem_galeria_3 = models.ImageField(
        upload_to='projeto/imagem_galeria', blank=True
    )
    imagem_galeria_4 = models.ImageField(
        upload_to='projeto/imagem_galeria', blank=True
    )
    
    ativo = models.BooleanField(default=True)
    pos_destaque = models.IntegerField(blank=True, null=True, default=5)

    iframe = models.TextField(blank=True)
    
    data_criacao = models.DateTimeField(default=timezone.now, blank=False)

    @property
    def has_image(self):
        return self.imagem_inicio and self.imagem_inicio.name
    
    def __str__(self):
        return self.nome