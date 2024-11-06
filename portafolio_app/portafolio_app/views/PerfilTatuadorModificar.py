from django.shortcuts import render, redirect, get_object_or_404
from portafolio_app.db.models import portafolio, tatuador, diseños
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def load(request, tatuador_id):
    tatuador_obj = get_object_or_404(tatuador, pk=tatuador_id)
    portafolios = portafolio.objects.filter(tatuador=tatuador_obj)
    disenos = diseños.objects.filter(tatuador=tatuador_obj)

    if request.method == 'POST':
        # Actualizar datos del tatuador si se envían cambios
        nombre = request.POST.get('nombre')
        telefono_valor = request.POST.get('telefono')
        edad = request.POST.get('edad')

        persona = tatuador_obj.persona
        if nombre:
            persona.nombre = nombre
        if edad:
            persona.edad = edad
        persona.save()

        telefono = tatuador_obj.telefono
        if telefono_valor:
            telefono.telefono = telefono_valor
        telefono.save()

        # Obtener el ID del portafolio a eliminar
        portafolio_id = request.POST.get('portafolio_id')
        if portafolio_id:
            # Eliminar el portafolio
            portafolio.objects.filter(pk=portafolio_id, tatuador=tatuador_obj).delete()
            # Redirigir a la misma página después de la eliminación
            return redirect('PerfilTatuadorModificar', tatuador_id=tatuador_id)

        # Procesar el formulario para agregar un nuevo portafolio
        titulo_nuevo = request.POST.get('titulo_nuevo')
        descripcion_nueva = request.POST.get('descripcion_nueva')
        foto_nueva = request.POST.get('foto_nueva')

        if titulo_nuevo and descripcion_nueva and foto_nueva:
            nuevo_portafolio = portafolio(
                titulo=titulo_nuevo,
                descripcion=descripcion_nueva,
                foto=foto_nueva,
                tatuador=tatuador_obj
            )
            nuevo_portafolio.save()

        # Obtener el ID del diseño a eliminar
        disenos_id = request.POST.get('disenos_id')
        if disenos_id:
            # Eliminar el diseño
            diseños.objects.filter(pk=disenos_id, tatuador=tatuador_obj).delete()
            # Redirigir a la misma página después de la eliminación
            return redirect('PerfilTatuadorModificar', tatuador_id=tatuador_id)

        # Procesar el formulario para agregar un nuevo diseño
        titulo_nuevos = request.POST.get('titulo_nuevos')
        descripcion_nuevas = request.POST.get('descripcion_nuevas')
        estilo_nuevos = request.POST.get('estilo_nuevos')
        foto_nuevas = request.POST.get('foto_nuevas')

        if titulo_nuevos and descripcion_nuevas and foto_nuevas and estilo_nuevos:
            nuevo_diseño = diseños(
                titulo=titulo_nuevos,
                descripcion=descripcion_nuevas,
                foto=foto_nuevas,
                estilo=estilo_nuevos,
                tatuador=tatuador_obj
            )
            nuevo_diseño.save()

        # Después de procesar el formulario, redirigir a la misma página para evitar reenvíos de formulario
        return redirect('PerfilTatuadorModificar', tatuador_id=tatuador_id)

    # Si el método HTTP no es POST o no se envió el formulario, simplemente renderiza la página con los datos actuales
    context = {'portafolios': portafolios, 'tatuador': tatuador_obj, 'disenos': disenos}
    return render(request, 'PerfilTatuadorModificar.html', context)