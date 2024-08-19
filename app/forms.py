from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password'}),
        help_text='Coloque sua senha.'
    )
    password2 = forms.CharField(
        label='Confirme sua senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password2'}),
        help_text='Coloque a mesma senha.'
    )

    class Meta:
        model = User
        fields = ['username','password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2:
            # Verifica se as senhas coincidem
            if password1 != password2:
                raise ValidationError("As senhas não são iguais.")

            # Verifica o comprimento da senha
            if len(password2) < 8:
                raise ValidationError("A senha deve ter pelo menos 8 caracteres.")

        return password2
