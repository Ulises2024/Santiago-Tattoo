from django.shortcuts import render, redirect
from portafolio_app.db.models import reseña

def load(request):
    if request.method == 'POST':
        reseña_id = request.POST.get('reseñas_id')
        if reseña_id:
            reseña.objects.filter(pk=reseña_id).delete()
            return redirect('PerfilTatuador')    
# Obtener todos los objetos del modelo Reseñas
    reseñas = reseña.objects.all()
    # Pasar los objetos al contexto de la plantilla
    context = {'reseñas': reseñas}
    # Renderizar la plantilla 'tatuador.html' con el contexto
    return render(request, 'ReseñasPage.html', context)