from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class SkillCategory(models.Model):
    name = models.CharField(max_length=255)
    resumo = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)
    resumo = models.TextField()
    level = models.IntegerField(blank=True)
    imagem_inicio = models.ImageField(
        upload_to='skills/logos', blank=True, null=True
    )
    ativo = models.BooleanField(default=True)
    
    
    imagem_central = models.ImageField(
        upload_to='skills/imagem_central', blank=True, null=True
    )
    descricao = CKEditor5Field('descricao', config_name='extends', blank=True, null=True)
    ativo = models.BooleanField(default=True)
    pos_destaque = models.IntegerField(blank=True, null=True, default=5)
    skill_category = models.ForeignKey(SkillCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name