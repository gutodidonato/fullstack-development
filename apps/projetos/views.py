from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator


from ..projetos.models import Projeto, CategoriaProjeto
from ..skills.models import Skill


def projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    skills = projeto.skills.all()
    
    for skill in skills:
        print("skills:")
        print(skill)
    
    context = {
        'skills': skills,
        'projeto': projeto

    }
    return render(request, 'projetos/index.html', context)


from django.http import JsonResponse
from django.template.loader import render_to_string
from django.template.loader import render_to_string

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

def listagem_projeto(request, categoria_id=None):
    categorias = CategoriaProjeto.objects.filter(ativo=True)

    if categoria_id:
        categoria_selecionada = get_object_or_404(CategoriaProjeto, id=categoria_id)
        projetos = Projeto.objects.filter(categoria_projeto=categoria_selecionada.id, ativo=True)
    else:
        categoria_selecionada = None
        projetos = Projeto.objects.filter(ativo=True)

    paginator = Paginator(projetos, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # AJAX
        projects_html = render_to_string('projetos/_projetos_grid.html', {'projetos': page_obj})
        pagination_html = render_to_string('projetos/_pagination.html', {'projetos': page_obj})
        return JsonResponse({
            'projects_html': projects_html,
            'pagination_html': pagination_html,
        })
    
    context = {
        'projetos': page_obj,
        'categorias': categorias,
        'categoria_selecionada': categoria_selecionada,
    }
    return render(request, 'projetos/listagem.html', context)
