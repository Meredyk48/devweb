from django.shortcuts import render
from .models import Contato, Categoria
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def index(request):
    contatos = Contato.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'pages/index.html', {'contatos': contatos, 'categorias': categorias})


# class ContatoListView(ListView):
 #   model = Contato
  #  template_name = 'pages/index.html'
    # context_object_name = 'contatos'

@login_required(login_url='login')
def contato_detalhes(request, id):
    # contato = Contato.objects.get(id=id)
    # , {'contato': contato})
    return render(request, 'pages/contato_detalhes.html', {'contato': Contato.objects.get(id=id)})


def home(request):
    contatos = Contato.objects.all()
    return render(request, 'pages/home.html', {'contatos': contatos})
#    return render(request, 'pages/home.html')


@login_required(login_url='login')
def contatoform(request):
    categoria = Categoria.objects.all()
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        foto = request.FILES['foto']
        telefone = request.POST['telefone']
        cep = request.POST['cep']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        categoria = request.POST['categoria']

        contato = Contato(nome=nome, email=email, foto=foto, telefone=telefone,
                          cep=cep, cidade=cidade, estado=estado, Categoria_id=categoria)
        contato.save()
        print(contato)
        return HttpResponse('Contato cadastrado com sucesso!')

    else:
        categoria = Categoria.objects.all()
        return render(request, 'pages/contatoform.html', {'categorias': categoria})


def ver_imagem(request):
    contatos = Contato.objects.all()
    return render(request, 'pages/ver_imagem.html', {'contatos': contatos})
