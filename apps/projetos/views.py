from django.shortcuts import render, get_object_or_404, redirect
from ..projetos.models import Projeto, CategoriaProjeto
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

def listagem_projeto(request):
    return render(request, 'projetos/listagem.html')