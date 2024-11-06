from django.contrib import admin
from django.urls import path, include

# HABILITAR LOS DEMÁS MODEL DE DJANGO EN EL ADMIN
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


from .views import logout
from .views import loginpage
from .views import index
from .views.send_email import send_email


from usuarios.views import register, calendar_view, crear_cita, eliminar_cita, calendar_view_cliente, editar_cita, nosotros_view
from .views import portafoliopage
from .views import ReseñasPage
from.views import PerfilTatuador
from.views import PerfilUsuario
from .views import PerfilTatuadorModificar
from .views import PerfilUsuarioModificar
#from .views import enviar_correo_contacto
from .db.models import region, provincia, comuna
from .db.models import persona, emails, telefono, direccion, cliente
from .db.models import estudio, tatuador, reseña, portafolio, diseños
from .db.models import materiales, cita, factura, metodo_pago, transacciones, detalle_factura


# ADD MODEL IN ADMIN
admin.site.register(Permission)
admin.site.register(ContentType)
admin.site.register(region)
admin.site.register(provincia)
admin.site.register(comuna)
admin.site.register(persona)
admin.site.register(emails)
admin.site.register(telefono)
admin.site.register(direccion)
admin.site.register(cliente)
admin.site.register(estudio)
admin.site.register(tatuador)
admin.site.register(reseña)
admin.site.register(portafolio)
admin.site.register(diseños)
admin.site.register(materiales)
admin.site.register(cita)
admin.site.register(factura)
admin.site.register(metodo_pago)
admin.site.register(transacciones)
admin.site.register(detalle_factura)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout', logout.load, name= "logout"),
    path('', index.index),
    path('index/',index.index, name = "index"),
    path('usuarios/', include('usuarios.urls'), name = "reg"),
    path('accounts/login/', loginpage.load),   
    path('loginpage', loginpage.load, name = "loginpage"),
    path ( 'portafolio', portafoliopage.load),
    path ( 'reseñas', ReseñasPage.load),
    path('PerfilTatuador/<int:tatuador_id>/',PerfilTatuador.load , name='PerfilTatuador'),
    path ( 'PerfilUsuario', PerfilUsuario.load, name = "PerfilUsuario"),
    path('send-email/', send_email, name='send_email'),
    path ( 'PerfilTatuadorModificar/<int:tatuador_id>/', PerfilTatuadorModificar.load , name = "PerfilTatuadorModificar"),
    path ( 'PerfilUsuarioModificar', PerfilUsuarioModificar.load , name = "PerfilUsuarioModificar"),
    path('calendar/', calendar_view, name='calendar-view'),
    path('calendar_cliente/', calendar_view_cliente, name='calendar-cliente'),
    path('calendar/crear_cita/', crear_cita, name='crear_cita'),
    path('calendar/eliminar_cita/<int:id>/', eliminar_cita, name='eliminar_cita'),
    path('calendar/editar_cita/<int:id>/', editar_cita, name='editar_cita'),
    path('nosotros/', nosotros_view, name='nosotros'),
    ]
