from django.db import models

# Create your models here.
class personajes(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    estado = models.CharField(max_length=50, verbose_name="Estado" , choices=[('Alive', 'Vivo'), ('Dead', 'Muerto'), ('unknown', 'Desconocido',)])
    especies = models.CharField(max_length=100, verbose_name="Especie")
    genero = models.CharField(max_length=50, verbose_name="Genero",choices=[('Female', 'Mujer'), ('Male', 'Hombre'), ('Genderless', 'Sin género'), ('unknown', 'Desconocido')])
    origen = models.CharField(max_length=255, blank=True, null=True,verbose_name="Origen")
    ubicacion = models.CharField(max_length=200,blank=True, null=True, verbose_name="Ubicación")
    imagen = models.URLField(verbose_name="Imagen")
    URL = models.URLField(blank=True, null=True,verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")

    class Meta:
        db_table = 'Rick y Morty'
        verbose_name = "Personaje"
        verbose_name_plural = "Personajes"
        ordering = ['-created']


    def __str__(self):
        return self.nombre  
    