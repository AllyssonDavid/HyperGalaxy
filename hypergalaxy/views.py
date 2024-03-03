from django.shortcuts import render, redirect
from hypergalaxy.models import Projeto, Funcionario, ImagesProject
from blog.models import Post
from hypergalaxy.forms import FormContato
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# Create your views here.


def index(request):
    projetos = Projeto.objects.order_by('titulo').filter(publicado=True)
    funcionarios = Funcionario.objects.order_by('nome')
    posts = Post.objects.filter(publicado=True, destaque=False).order_by('created_at')[:2]
    return render(request, 'index.html', {
        'projetos':projetos, 
        'funcionarios': funcionarios,
        'posts': posts,
        'pagina': 'Home'
    })
    
def projeto_padrao(request):
    return render(request, 'projeto-padrao.html', {'pagina': 'Projeto Padrão'})

def contato(request):
    form = FormContato()
    return render(request, 'contato.html', {
        'pagina':'Contato',
        'form':form
    })

    
def send_email(request):
    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            nome = form.data['nome']
            email = form.data['email']
            assunto = form.data['assunto']
            servicos = form.data['servico']
            context = {'nome': nome, 'email': email, 'servicos': servicos,'assunto': assunto}
            html_content = render_to_string('email_templates/sendmail.html', context)
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                subject=f'Cliente | {nome}',
                body=text_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.DEFAULT_FROM_EMAIL]
            )

            email.attach_alternative(html_content, 'text/html') 
            email.send()
            
            messages.success(request, 'Obrigado😊! Mensagem enviada com sucesso!')
            return redirect('contato')
        else:
            messages.error(request, 'Opss 😢, não foi possivel enviar a mensagem!')
            return redirect('contato')
    
    

def sobre(request):
    return render(request, 'sobre.html', {
        'pagina': 'sobre'
    })
    
def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {
        'projetos':projetos,
        'pagina': 'Projetos'
    })
    
def projeto(request, projeto_id:int):
    projeto = Projeto.objects.get(pk=projeto_id)
    images = ImagesProject.objects.filter(projeto_id=projeto_id)
    return render(request, 'detalhes_cases.html', {
        'projeto':projeto,
        'images':images,
        'pagina': projeto.titulo
    })
    
def equipe(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'equipe.html', {
        'funcionarios':funcionarios,
        'pagina': 'Equipe Hyper'
    })
    
def colaborador(request, colaborador_id:int):
    funcionario = Funcionario.objects.get(pk=colaborador_id)
    return render(request, 'detalhe_colaborador.html', {
        'funcionario':funcionario,
        'pagina': funcionario.nome
    })
    
def page_not_found(request, exception):
    return render(request, '404.html', {
        'pagina': '404 not found'
    }, status=404)