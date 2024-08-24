from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm as CustomAuthenticationForm
from .forms import UserRegistrationForm
from django.urls import path
from .models import Funcionario
from django.shortcuts import render, get_object_or_404
from . import views
import json

def minha_view(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')  # Redirecione para uma URL válida
    else:
        form = CustomAuthenticationForm()
    return render(request, 'index.html', {'form': form})

def principal_view(request):
    return render(request, 'main.html')

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    print(funcionarios)
    return render(request, 'main.html', {'funcionarios': funcionarios})



def funcionario_detalhes(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'skills.html', {'funcionario': funcionario})

