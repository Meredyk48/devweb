from django.contrib import admin

# Register your models here.
from .models import Contato


@admin.register(Contato)
class AdminContato(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cep',
                    'cidade', 'estado', 'data_criacao')
    list_filter = ('cidade', 'estado', 'data_criacao')
