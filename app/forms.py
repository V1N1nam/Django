from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import CalendarioItem, Funcionario

class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_username', 'placeholder': 'Digite seu nome de usuário'}),
    label='Nome de usuário'
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password', 'placeholder': 'Crie uma senha'}),
        help_text='Coloque sua senha.'
    )
    password2 = forms.CharField(
        label='Confirme sua senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password2', 'placeholder': 'Confirme sua senha'}),
        help_text='Coloque a mesma senha.'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2:
            if password1 != password2:
                raise ValidationError("As senhas não são iguais.")
            
        return password2

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_username'}),
        label='Nome de usuário'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password'}),
        label='Senha'
    )

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cargo', 'data_nascimento', 'skills']

    data_nascimento = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'dd/mm/aaaa'})
    )

class CalendarioItemForm(forms.ModelForm):
    class Meta:
        model = CalendarioItem
        fields = ['data_inicio', 'data_fim', 'titulo', 'descricao']