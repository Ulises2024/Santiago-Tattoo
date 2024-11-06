from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.forms import widgets

from django.forms.models import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from portafolio_app.db.models import Contacto
from portafolio_app.db.models import tatuador
from portafolio_app.db.models import cita
from portafolio_app.db.models import cliente
from portafolio_app.db.models import estudio
from portafolio_app.db.models import DetallePago


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



class ContactoForm(forms.ModelForm):
    tatuador = forms.ModelChoiceField(queryset=tatuador.objects.all(), empty_label="Seleccione un tatuador")
    
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellido', 'email', 'tatuador', 'mensaje']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
            'tatuador': 'Tatuador',
            'mensaje': 'Mensaje',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'pattern': '[a-zA-Z ]{3,50}', 'class': 'form-control nombre_input', 'placeholder': 'Ingrese su nombre', 'id': 'nombre'}),
            'apellido': forms.TextInput(attrs={'pattern': '[a-zA-Z ]{3,50}', 'class': 'form-control apellido_input', 'placeholder': 'Ingrese su apellido', 'id': 'apellido'}),
            'email': forms.EmailInput(attrs={'pattern': '[a-z0-9._-]{8,16}@(tattoo|gmail|hotmail|duocuc)\.(com|cl|es|ar)', 'class': 'form-control email_input', 'placeholder': 'Ingrese su correo electrónico', 'id': 'correo_e'}),
            'tatuador': forms.Select(attrs={'class': 'form-control tatuador_input', 'placeholder': 'Seleccione el tatuador', 'id': 'id_tatuador'}),
            'mensaje': forms.TextInput(attrs={'pattern': '[a-zA-Z ]{20,500}', 'class': 'form-control mensaje_text', 'placeholder': 'Ingrese su mensaje', 'id': 'id_mensaje'}),
        }





class CitaForm(forms.ModelForm):
    tatuador = forms.ModelChoiceField(queryset=tatuador.objects.all(), empty_label="Seleccione un tatuador")
    cliente = forms.ModelChoiceField(queryset=cliente.objects.all(), empty_label="Seleccione un cliente")
    estudio = forms.ModelChoiceField(queryset=estudio.objects.all(), empty_label="Seleccione un estudio")

    class Meta:
        model = cita
        fields = ['eventTitle', 'eventStartDate', 'eventEndDate', 'eventStartTime', 'eventEndTime', 'descripcion', 'tatuador', 'estudio', 'cliente']

        labels = {
            'eventTitle': 'Título del Evento', 
            'eventStartDate': 'Fecha de Inicio', 
            'eventEndDate': 'Fecha de Fin', 
            'eventStartTime': 'Hora de Inicio', 
            'eventEndTime': 'Hora de Fin', 
            'descripcion': 'Descripción', 
            'tatuador': 'Tatuador', 
            'estudio': 'Estudio',
            'cliente': 'Cliente',
        }
        
        widgets = {
            'eventTitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título del evento'}),
            'eventStartDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'eventEndDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'eventStartTime': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'eventEndTime': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción del evento', 'rows': 5}),
            'tatuador': forms.Select(attrs={'class': 'form-control tatuador_input', 'placeholder': 'Seleccione el tatuador', 'id': 'id_tatuador'}),
            'estudio': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el estudio'}),
            'cliente': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el cliente'}),
        }

class EliminarCitaForm(forms.Form):
    cita_title = forms.ModelChoiceField(queryset=cita.objects.all(), empty_label="Seleccione una cita")
    
    def clean(self):
        cleaned_data = super().clean()
        cita_title = cleaned_data.get("cita_title")

        if not cita_title:
            raise forms.ValidationError("Debe proporcionar el título de la cita.")
        
        return cleaned_data


class PagoForm(forms.ModelForm):
    class Meta:
        model = DetallePago
        fields = ['abono', 'cita', 'estado', 'fecha']

        labels = {
            'abono': 'Abono',
            'cita': 'Cita',
            'estado': 'Estado',
            'fecha': 'Fecha',
        }

        widgets = {
            'abono': forms.NumberInput(attrs={'pattern': '[0-9]{3,50}','class': 'form-control'}),
            'cita': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
