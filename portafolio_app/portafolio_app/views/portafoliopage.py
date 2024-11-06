from django.shortcuts import render
from portafolio_app.db.models import portafolio

def load(request):
# Obtener todos los objetos del modelo Portafolio
    portafolios = portafolio.objects.all()
    # Pasar los objetos al contexto de la plantilla
    context = {'portafolios': portafolios}
    # Renderizar la plantilla 'tatuador.html' con el contexto
    return render(request, 'portafoliopage.html', context)