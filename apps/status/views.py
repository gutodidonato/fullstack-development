from django.shortcuts import redirect, render
#from smtp import enviar_mensagem
from ..status.forms import ContactForms
from django.contrib import messages

from ..skills.models import Skill, SkillCategory
from ..status.models import Status
from ..projetos.models import Projeto
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):

    status_destaque = Status.objects
    projetos_destaque = Projeto.objects.filter(ativo=True).order_by('pos_destaque')[:3]
    
    try:
        linguagem_categoria = SkillCategory.objects.get(name="linguagem")
        skills_linguagem = Skill.objects.filter(
            skill_category=linguagem_categoria,
            ativo=True)
    
        
        poderes_framework_categoria = SkillCategory.objects.get(name="poder")
        skills_framework = Skill.objects.filter(
            skill_category=poderes_framework_categoria,
            ativo=True)
        
        ferramentas = SkillCategory.objects.get(name="ferramenta")
        skill_ferramenta = Skill.objects.filter(
            skill_category=ferramentas,
            ativo=True
        )
    
    except:
        skills_linguagem = []
        skills_framework = []
        skill_ferramenta = []
    
    
    
    
    
    for skill in skills_linguagem:
        print(skill.imagem_inicio.url)
    
    
    print(skill_ferramenta)
    print(skills_framework)
    print(skills_linguagem)
    context = {
        'status_destaque': status_destaque,
        'projetos_destaque': projetos_destaque,
        
        
        'linguagens': skills_linguagem,
        'poderes': skills_framework,
        'ferramentas': skill_ferramenta,

        
        'time_ferramentas': len(skill_ferramenta) *3,
        'time_poderes': len(skills_framework) * 3,
        'time_linguagens': len(skills_linguagem) * 3
    }
    
    return render(request, 'base/index.html', context)




@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            send_mail(
                subject=f"Mensagem de {name}",
                message=message + '\n\nEmail: ' + email,
                from_email='gutodidonato@gmail.com',  
                recipient_list=['gutodidonato@gmail.com'],  
            )
            return redirect('index')
        except Exception as e:
            return JsonResponse({'error': f'Erro ao enviar email: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método não permitido'}, status=405)

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
