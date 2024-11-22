from django.db import models
from ..skills.models import Skill
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

class Projeto(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    resumo = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill, related_name='projeto', blank=True)
    imagem_inicio = models.ImageField(
        upload_to='projeto/start', blank=True
    )
    link_github= models.CharField(max_length=255, blank=True)
    link_demo= models.CharField(max_length=255, blank=True)
    
    
    
    imagem_central = models.ImageField(
        upload_to='projeto/imagem_central', blank=True
    )
    descricao = CKEditor5Field(
        'descricao', config_name='extends'
    )
    ativo = models.BooleanField(default=True)
    pos_destaque = models.IntegerField(blank=True, null=True, default=5)

    iframe = models.TextField(blank=True)
    
    data_criacao = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.nome