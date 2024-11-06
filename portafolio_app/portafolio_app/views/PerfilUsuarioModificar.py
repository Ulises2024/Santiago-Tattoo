from django.shortcuts import render
from portafolio_app.db.models import cliente
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def load(request):
    if request.user.is_authenticated:
        user = request.user
        # Verificamos si el usuario tiene un correo electrónico asociado
        if user.email:
            # Buscamos el cliente asociado al correo electrónico del usuario
            try:
                cliente_usuario = cliente.objects.get(emails__mail=user.email)

                if request.method == 'POST':
                    # Imprime los datos POST para depuración
                    print(request.POST)

                    # Actualizar datos del tatuador si se envían cambios
                    nombre = request.POST.get('nombre')
                    telefono_valor = request.POST.get('telefono')
                    edad = request.POST.get('edad')

                    persona = cliente_usuario.persona
                    if nombre:
                        persona.nombre = nombre
                    if edad:
                        persona.edad = edad
                    persona.save()

                    telefono = cliente_usuario.telefono
                    if telefono_valor:
                        telefono.telefono = telefono_valor
                    telefono.save()

                return render(request, 'PerfilUsuarioModificar.html', {'cliente': cliente_usuario})
            except cliente.DoesNotExist:
                # Manejar el caso en que no se encuentre un cliente asociado al correo electrónico
                return render(request, 'PerfilUsuarioModificar.html', {'error': 'No se encontró un cliente asociado a este usuario.'})
        else:
            # Manejar el caso en que el usuario no tenga correo electrónico
            return render(request, 'PerfilUsuarioModificar.html', {'error': 'El usuario no tiene un correo electrónico asociado.'})
    else:
        # Manejar el caso en que el usuario no esté autenticado
        return render(request, 'PerfilUsuarioModificar.html', {'error': 'El usuario no está autenticado.'})