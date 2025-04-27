from django.db import models

# Create your models here.
from django.db import models

class personajes(models.Model):
    nombre = models.CharField(max_length=255)
    estado = models.CharField(max_length=50, choices=[('Alive', 'Vivo'), ('Dead', 'Muerto'), ('unknown', 'Desconocido')])
    especies = models.CharField(max_length=100)
    genero = models.CharField(max_length=50, choices=[('Female', 'Mujer'), ('Male', 'Hombre'), ('Genderless', 'Sin género'), ('unknown', 'Desconocido')])
    origen = models.CharField(max_length=255, blank=True, null=True)
    ubicacion = models.CharField(max_length=200,blank=True, null=True)
    imagen = models.URLField()
    URL = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
