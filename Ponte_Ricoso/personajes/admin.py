from django.contrib import admin
from .models import personajes  

# Register your models here.
class personajesAdmin(admin.ModelAdmin):
    fields = ['nombre', 'estado', 'especies', 'genero', 'origen', 'ubicacion', 'imagen', 'URL']
    list_display = ['nombre', 'estado', 'especies', 'genero', 'origen', 'ubicacion']

admin.site.register(personajes, personajesAdmin)