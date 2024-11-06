from django.contrib import admin
from portafolio_app.db.models import Contacto
from portafolio_app.db.models import cita


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'fecha', 'tatuador', 'mensaje')
    search_fields = ('nombre', 'apellido', 'email', 'mensaje')
    list_filter = ('tatuador', 'fecha')

