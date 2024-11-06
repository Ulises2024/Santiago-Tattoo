from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import Producto, Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido Paterno',
            'email': 'Correo Electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre de usuario', 'id': 'username'}),
            'first_name': forms.TextInput(attrs={'pattern': '[a-zA-Z]{3,25}', 'class': 'form-control', 'placeholder': 'Ingrese su nombre', 'id': 'first_name'}),
            'last_name': forms.TextInput(attrs={'pattern': '[a-zA-Z]{3,25}', 'class': 'form-control', 'placeholder': 'Ingrese su apellido paterno', 'id': 'last_name'}),
            'email': forms.EmailInput(attrs={'pattern': '[a-z0-9._-]{8,16}@(patitas|gmail|hotmail|duocuc)\.(com|cl|es|ar)', 'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico', 'id': 'email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña', 'id': 'password1'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme su contraseña', 'id': 'password2'}),
        }


