from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from .forms import RegistroUserForm, ContactoForm, CitaForm, PagoForm
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from portafolio_app.db.models import cita, persona, tatuador, cliente, emails, DetallePago
from django.core import serializers
from .forms import EliminarCitaForm
from django.contrib.auth.models import Group
from .functions import generateAccessToken
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistroUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name = "clientes")
            user.groups.add(group)
            user.save(force_update=True)
            return redirect('index')
    else:
        form = RegistroUserForm()
    return render(request, 'registrar.html', {'form': form})

def base(request):
    return render(request, 'base.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu mensaje ha sido enviado exitosamente.')
            return redirect(reverse('contacto'))
        else:
            messages.error(request, 'Hubo un error al enviar tu mensaje. Por favor, intenta de nuevo.')
            return redirect(reverse('contacto'))
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})




@login_required
def calendar_view(request):
    citas = cita.objects.all()
    cita_json = serializers.serialize('json', citas)
    context = {
        'citas': citas,
        'cita_json': cita_json,
        'is_staff': request.user.is_staff
    }
    return render(request, 'calendar.html', context)


@login_required
def calendar_view_cliente(request):
    # Capturar el email del usuario logueado
    user_email = request.user.email

    # Buscar el email en la tabla emails y obtener el persona_id
    try:
        email_entry = emails.objects.get(mail=user_email)
        persona_id = email_entry.persona_id
    except emails.DoesNotExist:
        persona_id = None
        cliente_id = None
    else:
        # Si el persona_id es encontrado, buscar en la tabla cliente
        try:
            cliente_entry = cliente.objects.get(persona_id=persona_id)
            cliente_id = cliente_entry.id
        except cliente.DoesNotExist:
            cliente_id = None

    # Obtener todas las citas del cliente logueado
    if cliente_id is not None:
        citas = cita.objects.filter(cliente_id=cliente_id)
    else:
        citas = cita.objects.none()

    # Serializar las citas
    cita_json = serializers.serialize('json', citas)

    # Pasar el email del usuario, persona_id, cliente_id y citas al contexto
    return render(request, 'calendar_cliente.html', {
        'citas': citas,
        'cita_json': cita_json,
        'user_email': user_email,
        'persona_id': persona_id,
        'cliente_id': cliente_id
    })


@login_required
def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            try:
                cita_instance = form.save()
                return redirect('pagar')
            except ValidationError as e:
                form.add_error(None, e.message)  # agrega el mensaje de error al formulario
        else:
            return redirect('cita_fallida')
    else:
        form = CitaForm()
    return render(request, 'crear_cita.html', {'form': form})
    

@login_required
def eliminar_cita(request, id):
    # Obtener todas las citas
    citas = cita.objects.all()
    # Extraer los IDs de las citas
    cita_ids = [cita.id for cita in citas]
    
    # Comparar el ID recibido con los IDs de las citas
    if id in cita_ids:
        # Filtrar la cita específica y eliminarla
        cita_filtro = get_object_or_404(cita, id=id)
        cita_filtro.delete()
        mensaje = f"Cita con ID {id} eliminada exitosamente."
        return render(request, 'eliminar_cita.html', {'cita_ids': cita_ids, 'mensaje': mensaje})
    else:
        # Devolver un mensaje indicando que el evento no se encuentra en la base de datos
        mensaje = f"Cita con ID {id} no se encuentra en la base de datos."
    
    # Redirigir a la plantilla y pasar la lista de IDs y el mensaje
    return render(request, 'eliminar_cita.html', {'cita_ids': cita_ids, 'mensaje': mensaje})


@login_required
def editar_cita(request, id):
    # Obtener todas las citas
    citas = cita.objects.all()
    # Extraer los IDs de las citas
    cita_ids = [cita.id for cita in citas]
    
    # Comparar el ID recibido con los IDs de las citas
    if id in cita_ids:
        # Filtrar la cita específica
        cita_filtro = get_object_or_404(cita, id=id)
        
        # Verificar si el formulario ha sido enviado
        if request.method == "POST":
            form = CitaForm(request.POST, instance=cita_filtro)
            if form.is_valid():
                form.save()
                mensaje = "Cita actualizada exitosamente."
                return render(request, 'editar_cita.html', {'form': form, 'mensaje': mensaje})
        else:
            # Inicializar el formulario con los datos de la cita
            form = CitaForm(instance=cita_filtro)
    else:
        # Devolver un mensaje indicando que el evento no se encuentra en la base de datos
        mensaje = f"Cita con ID {id} no se encuentra en la base de datos."
        form = None
    
    return render(request, 'editar_cita.html', {'form': form, 'mensaje': mensaje if form is None else None})

        

def cliente_user(request):
    if request.user.is_authenticated:
        user = request.user

        if user.email:
            try:
                cliente_usuario = cliente.objects.get(emails__mail=user.email)
                return render(request, 'crear_cita.html',{'cliente':cliente_usuario})
            except cliente.DoesNotExist:
                return render(request, 'crear_cita.html',{'error':' No se encontro un cliente asociado a este usuario'})
        else:
            return render(request, 'crear_cita.html',{'error':' El usuario no tiene un correo electronico asociado.'})
    
    else:
        return render(request, 'crear_cita.html', {'error':' El usuario no esta registrado.'})


def cita_exitosa(request):
    return render(request, 'cita_exitosa.html')

def cita_fallida(request):
    return render(request, 'cita_fallida.html')

@login_required
def cita_eliminada(request):
    return render(request, 'cita_eliminada.html')


def nosotros_view(request):
    return render(request, 'nosotros.html')

@login_required
def pagar_view(request, cita_id=None):
    user_email = request.user.email
    print("User email:", user_email)

    cliente_id = None
    try:
        email_entry = emails.objects.get(mail=user_email)
        persona_id = email_entry.persona_id
        print("Persona ID:", persona_id)

        cliente_entry = cliente.objects.get(persona_id=persona_id)
        cliente_id = cliente_entry.id
        print("Cliente ID:", cliente_id)
    except (emails.DoesNotExist, cliente.DoesNotExist):
        pass

    ultima_cita = None
    if cliente_id is not None:
        ultima_cita = cita.objects.filter(cliente_id=cliente_id).order_by('-id').first()
        if ultima_cita:
            print("Última Cita:", ultima_cita.id)
        else:
            print("No se encontró ninguna cita para el cliente.")

    if cita_id is None and ultima_cita:
        return redirect('pagar_view', cita_id=ultima_cita.id)

    if cita_id:
        ultima_cita = get_object_or_404(cita, id=cita_id)

    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cita_exitosa')  # Ajusta según tu ruta
            
    else:
        initial_data = {'estado': 'No pagado', 'fecha': timezone.now()}
        if ultima_cita:
            initial_data['cita'] = ultima_cita
        form = PagoForm(initial=initial_data)
    
    return render(request, 'pagar.html', {'form': form, 'cita': ultima_cita})
