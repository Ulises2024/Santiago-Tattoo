from django.urls import path
from .views import register, base, contacto, crear_cita, cliente_user, cita_exitosa, cita_eliminada, editar_cita, nosotros_view, cita_fallida, pagar_view



urlpatterns = [
    path('registrar/', register, name='register'),
    path('base/', base, name='base'),
    path('contacto/', contacto, name='contacto'),
    path('nosotros/', nosotros_view, name='nosotros'),
    path('crear_cita/', crear_cita, name='crear_cita'),
    path('crear_cita/cliente_user', cliente_user, name='cliente_user'),
    path('cita_exitosa/', cita_exitosa, name='cita_exitosa'),
    path('cita_eliminada/', cita_eliminada, name='cita_eliminada'),
    path('calendar/editar_cita/<int:id>/', editar_cita, name='editar_cita'),
    path('calendar/crear_cita/pagar/', pagar_view, name='pagar'),
    path('calendar/crear_cita/pagar/<int:cita_id>/', pagar_view, name='pagar_view'),
    path('calendar/crear_cita/cita_fallida/', cita_fallida, name='cita_fallida'),

]
