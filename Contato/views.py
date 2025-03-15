from django.shortcuts import render
from .models import Contato
from django.views.generic import ListView
from django.http import HttpResponse
# Create your views here.


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'pages/index.html', {'contatos': contatos})

# class ContatoListView(ListView):
 #   model = Contato
  #  template_name = 'pages/index.html'
    # context_object_name = 'contatos'


def contato_detalhes(request, id):
    # contato = Contato.objects.get(id=id)
    # , {'contato': contato})
    return render(request, 'pages/contato_detalhes.html', {'contato': Contato.objects.get(id=id)})


def home(request):
    contatos = Contato.objects.all()
    return render(request, 'pages/home.html', {'contatos': contatos})
#    return render(request, 'pages/home.html')
