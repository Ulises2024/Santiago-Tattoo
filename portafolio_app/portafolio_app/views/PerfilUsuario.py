from django.shortcuts import render
from portafolio_app.db.models import cliente

def load(request):
    if request.user.is_authenticated:
        user = request.user
        # Verificamos si el usuario tiene un correo electrónico asociado
        if user.email:
            # Buscamos el cliente asociado al correo electrónico del usuario
            try:
                cliente_usuario = cliente.objects.get(emails__mail=user.email)
                return render(request, 'PerfilUsuario.html', {'cliente': cliente_usuario})
            except cliente.DoesNotExist:
                # Manejar el caso en que no se encuentre un cliente asociado al correo electrónico
                return render(request, 'PerfilUsuario.html', {'error': 'No se encontró un cliente asociado a este usuario.'})
        else:
            # Manejar el caso en que el usuario no tenga correo electrónico
            return render(request, 'PerfilUsuario.html', {'error': 'El usuario no tiene un correo electrónico asociado.'})
    else:
        # Manejar el caso en que el usuario no esté autenticado
        return render(request, 'PerfilUsuario.html', {'error': 'El usuario no está autenticado.'})