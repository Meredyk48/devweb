from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
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


def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request):

    if request.method == "POST":
        usuario = request.POST['usuario']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        if User.objects.filter(username=usuario).exists():
            messages.error(
                request, "Nome de usuário já existe. Escolha outro.")
            return redirect('register')

        User.objects.create_user(username=usuario, email=email, password=senha)
        messages.success(request, "Usuário criado com sucesso!")
        return redirect('login')

    else:
        return render(request, 'pages/register.html')
