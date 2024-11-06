from django.shortcuts import render, redirect, get_object_or_404
from portafolio_app.db.models import portafolio, tatuador, reseña, diseños, cliente
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def load(request, tatuador_id):
    t = get_object_or_404(tatuador, pk=tatuador_id)
    portafolios = portafolio.objects.filter(tatuador=t)
    reseñas = reseña.objects.filter(tatuador=t)
    disenos = diseños.objects.filter(tatuador=t)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        cuerpo = request.POST.get('cuerpo')
        calificacion = request.POST.get('calificacion')
        
        # Validación básica de datos
        if not titulo or not cuerpo or not calificacion:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('PerfilTatuador', tatuador_id=tatuador_id)
        
        # Validar que la calificación sea un número entero
        try:
            calificacion = int(calificacion)
        except ValueError:
            messages.error(request, "La calificación debe ser un número entero.")
            return redirect('PerfilTatuador', tatuador_id=tatuador_id)

        # Buscar el cliente por el email del usuario logueado
        try:
            cliente_obj = cliente.objects.get(persona__emails__mail=request.user.email)
        except cliente.DoesNotExist:
            messages.error(request, "Cliente no encontrado.")
            return redirect('PerfilTatuador', tatuador_id=tatuador_id)
        
        # Crear la nueva reseña
        nueva_reseña = reseña(
            titulo=titulo,
            cuerpo=cuerpo,
            calificacion=calificacion,
            cliente=cliente_obj,
            tatuador=t
        )
        nueva_reseña.save()
        messages.success(request, "Reseña agregada exitosamente.")
        return redirect('PerfilTatuador', tatuador_id=tatuador_id)

    context = {
        'portafolios': portafolios,
        'tatuador': t,
        'reseñas': reseñas,
        'disenos': disenos,
    }
    return render(request, 'PerfilTatuador.html', context)