from django.shortcuts import render, get_object_or_404, redirect
from ..projetos.models import Projeto
from django.core.paginator import Paginator



def projeto(request, nome_projeto):
    projeto = get_object_or_404( Projeto, nome=nome_projeto)
    return render(request, 'projeto.html', {'projeto': projeto})


def projetos(request):
    projetos = Projeto.objects.all().order_by('data_criacao')
    paginator = Paginator(projetos, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = {
        'projetos': page_obj,
    }
    
    return render(request, '', contexto)