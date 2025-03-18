1º python -m venv venv # CRIA AMBIENTE VIRTUAL
--
2º .\venv\Scripts\activate # ATIVA O AMBIENTE VIRTUAL
--
3º pip install django # INSTALA O DJANGO
--
4º python -m django startproject core . # Inicia os arquivos de configuração #projeto
--
5º > python manage.py startapp nome_app 
# inicia o aplicativo em settings, adicionar 
import os
e em INSTALLED_APPS adicionar 'nome_app',
em templates [linha 60] 
'DIRS': [os.path.join(BASE_DIR, 'templates')]

em `urls` adicionar 
import django.urls path 

em urlpatterns, adicionar 
include path('', include('nome_app.urls')). 

Em models criar a classe e abaixo 

def __str__(self): 
    return self.nome 
    
Em admin
from .models import nome_classe 
e adicionar 
admin.site... 

views renderizam o html na tela, from django.shortcuts import render, depois, def index(request, 'pages/index.html'): return...


urls.py: from django.urls import path, from . import views, depois, urlpatterns = [ path('', views.index, name='index')

pasta templates com pasta pages dentro, criar arquivos .html
--
6º python manage.py makemigrations
--
7º python manage.py migrate

OBS: `python manage.py migrate` para alterações no banco.
--
8º 6º python manage.py create superuser # Configurar superusuário
--
9º python manage.py runserver # Endpoint /admin para acessar
--
10º em views.py from .models import nome_classe, depois def index(request) nome_app = nome_classe.objects.all()
--

pip freeze > requirements.txt

pip install -r requirements.txt

criar .gitignore na raiz, dentro dele: venv .\venv \venv (em cada linha), db.sqlite3 .\db.sqlite3 (em cada linha)
--

em models.py, PARA TORNAR campos como opcional, adicionar (blank=true)

para criar categorias, utilize chaves estrangeiras, 

class categoria(models.Model):
    nome = models.Charfield(max_length=255)

    def __str__(self):
        return self.nome


em admin.py, 

from .models import nome_classe, nome_categoria

admin.site.register(nome_classe)
admin.site.register(nome_categoria)

`makemigrations`
`migrate`





