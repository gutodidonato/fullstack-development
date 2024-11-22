from django.contrib import admin

from ..skills.models import Skill, SkillCategory

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_category', 'ativo', 'pos_destaque',)
    search_fields= ('name', 'level', 'ativo', )
    list_filter = ('ativo', 'skill_category',)
    ordering = ('pos_destaque', 'level',)
    list_editable = ('ativo',)
    
@admin.register(SkillCategory)
class SkillCategory(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)