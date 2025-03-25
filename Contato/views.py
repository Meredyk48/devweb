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
