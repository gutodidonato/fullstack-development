from django.contrib import admin

from ..projetos.models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'resumo', 'ativo', 'pos_destaque', )
    list_filter = ('ativo', 'pos_destaque', )
    search_fields = ('nome', 'resumo', 'skills', )
    list_editable = ('ativo',)
    
    
