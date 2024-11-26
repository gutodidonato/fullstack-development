from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class SkillCategory(models.Model):
    name = models.CharField(max_length=255)
    resumo = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class PossibilidadeSkills(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)
    extensao_name = models.TextField(blank=True, null=True)
    skill_category = models.ForeignKey(SkillCategory, on_delete=models.SET_NULL, null=True)
    resumo = models.TextField()
    level = models.IntegerField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem_inicio = models.ImageField(
        upload_to='skills/logos', blank=True, null=True
    )
    
    
    
    
    descricao_1 = CKEditor5Field('descricao_1', config_name='extends', blank=True, null=True)
    possibilidades = models.ManyToManyField(
        PossibilidadeSkills, related_name='possibilidades', blank=True
    )
    imagem_1 = models.ImageField(
        upload_to='skills/imagens', blank=True, null=True
    )
    
    
    titulo_descricao_2 = models.TextField(null=True, blank=True)
    descricao_2 = CKEditor5Field('descricao_2', config_name='extends', blank=True, null=True)
    code_example_1 = models.TextField(blank=True)
    imagem_2 = models.ImageField(
        upload_to='skills/imagens', blank=True, null=True
    )
    
    titulo_descricao_3 = models.TextField(null=True, blank=True)
    descricao_3 = CKEditor5Field('descricao_3', config_name='extends', blank=True, null=True)
    code_example_2 = models.TextField(blank=True)
    imagem_3 = models.ImageField(
        upload_to='skills/imagens', blank=True, null=True
    )
    
    pos_destaque = models.IntegerField(blank=True, null=True, default=5)

    def __str__(self):
        return self.name
    
