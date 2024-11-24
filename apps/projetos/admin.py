from django.contrib import admin

from ..projetos.models import Projeto, CategoriaProjeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'resumo', 'ativo', 'pos_destaque', )
    list_filter = ('ativo', 'pos_destaque', )
    search_fields = ('nome', 'resumo', 'skills', )
    list_editable = ('ativo',)
    
    
@admin.register(CategoriaProjeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', )
    list_filter = ('nome', 'ativo', )
    search_fields = ('nome', 'ativo', )
    list_editable = ('ativo', )  
    list_display_links = ('nome', )