from django.shortcuts import render
#from smtp import enviar_mensagem
from ..status.forms import ContactForms
from django.contrib import messages

from ..skills.models import Skill, SkillCategory
from ..status.models import Status
from ..projetos.models import Projeto


def index(request):

    status_destaque = Status.objects
    projetos_destaque = Projeto.objects
    
    try:
        linguagem_categoria = SkillCategory.objects.get(name="linguagem")
        skills_linguagem = Skill.objects.filter(
            skill_category=linguagem_categoria,
            ativo=True)
        
        print(linguagem_categoria)
        print(skills_linguagem)
        
  
        '''
        
        framework_categoria = SkillCategory.objects.get(name="framework")
        skills_framework = Skill.objects.filter(
            skill_category=framework_categoria,
            ativo=True)
        '''
    except:
        skills_linguagem = []
        skills_framework = []
    
    
    
    
    
    
    
    
    context = {
        'status_destaque': status_destaque,
        'projetos_destaque': projetos_destaque,
        'linguagens': skills_linguagem,
        'time_linguagens': len(skills_linguagem) * 2
    }
    
    return render(request, 'base/index.html', context)

def projeto(request):
    return render(request, 'projetos/index.html')



'''def contato(request):
    form = ContactForms()
    
    if request.method == 'POST':
        form = ContactForms(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            telefone = form.cleaned_data.get('telefone')
            empresa = form.cleaned_data.get('empresa')
            numero_de_funcionarios = form.cleaned_data.get('numero_de_funcionarios')
            mensagem = form.cleaned_data.get('mensagem')
            
            assunto = f"Novo contado de {name} - {empresa}"
            mensagem_texto = f"Nome: {name}\nEmail: {email}\nTelefone: {telefone}\nEmpresa: {empresa}\nNúmero de funcionários: {numero_de_funcionarios}\nMensagem: {mensagem}"
            
            try:
                enviar_mensagem(
                    mensagem_texto=mensagem_texto,
                    sender='gutodidonato@gmail.com',  
                    assunto=assunto,
                    senha_pass_sv='--',  
                    destinatario='gutodidonato@gmail.com' 
                )
                messages.success(request, 'Mensagem enviada com sucesso!')
            except Exception as e:
                print(e)
                messages.error(request, 'Erro ao enviar mensagem. Tente novamente.')

            #return redirect('contato')  
        else:
            messages.error(request, 'Erro ao preencher o formulário.')
    return render(request, 'base/contato.html', {'form': form})'''
