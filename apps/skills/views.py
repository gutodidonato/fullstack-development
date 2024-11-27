from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from ..skills.models import Skill, SkillCategory


def skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    
    context = {
        'skills': skill

    }
    return render(request, 'skills/index.html', context)



def listagem_skill(request, categoria_id=None):
    categorias = SkillCategory.objects.filter(ativo=True)

    if categoria_id:
        categoria_selecionada = get_object_or_404(SkillCategory, id=categoria_id, ativo=True)
        skills = Skill.objects.filter(skill_category=categoria_selecionada, ativo=True)
    else:
        categoria_selecionada = None
        skills = Skill.objects.filter(ativo=True)

    paginator = Paginator(skills, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  
        skills_html = render_to_string('skills/_skills_grid.html', {'skills': page_obj})
        pagination_html = render_to_string('skills/_pagination.html', {'skills': page_obj})
        return JsonResponse({
            'skills_html': skills_html,
            'pagination_html': pagination_html,
        })
    
    context = {
        'skills': page_obj,
        'categorias': categorias,
        'categoria_selecionada': categoria_selecionada,
    }
    return render(request, 'skills/listagem.html', context)
