from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm
from .forms import UserRegistrationForm
import json

def minha_view(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def principal_view(request):
    return render(request, 'main.html')
