from django import forms
from .models import personajes


class PersonajesForm(forms.ModelForm):
    class Meta:
        model = personajes
        fields = ['nombre', 'estado', 'especies', 'genero', 'origen', 'ubicacion', 'imagen', 'URL']