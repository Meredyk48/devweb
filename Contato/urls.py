from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detalhes/<int:id>/', views.contato_detalhes, name='contato_detalhe'),
    path('contato/', views.index, name='contato'),
    path('contato/cadastro/', views.contatoform, name='contatoform'),
    path('ver_imagem/', views.ver_imagem, name='ver_imagem'),

]
