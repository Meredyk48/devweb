from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def login(request):
    if request.method == "POST":

        usuario = request.POST['usuario']
        senha = request.POST['senha']

        verificar_usuario = auth.authenticate(username=usuario, password=senha)

        if verificar_usuario != None:
            auth.login(request, verificar_usuario)

            return redirect('home')

        else:
            print("Usuario ou senha invalidos")
            return render(request, 'pages/login.html')
    else:
        return render(request, 'pages/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
