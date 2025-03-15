from django.db import models

# Create your models here.
from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
