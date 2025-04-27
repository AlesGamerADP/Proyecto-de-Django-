import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import personajes
from .forms import PersonajesForm

def lista_personajes(request):
    personajes_lista = personajes.objects.all()
    return render(request, 'personajes/lista_personajes.html', {'personajes': personajes_lista})

def detalle_personaje(request, id):
    personaje = get_object_or_404(personajes, id=id)
    return render(request, 'personajes/detalle_personaje.html', {'personaje': personaje})

def crear_personaje(request):
    personaje = None 
    form = PersonajesForm()

    if 'buscar' in request.GET:
        nombre_buscado = request.GET.get('buscar') 
        api_url = f"https://rickandmortyapi.com/api/character/?name={nombre_buscado}" 

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            if 'results' in data and data['results']:
                personaje_api = data['results'][0]
                form = PersonajesForm(initial={
                    'nombre': personaje_api['name'],
                    'estado': personaje_api['status'],
                    'especies': personaje_api['species'],
                    'genero': personaje_api['gender'],
                    'origen': personaje_api['origin']['name'] if personaje_api['origin'] else None,
                    'ubicacion': personaje_api['location']['name'] if personaje_api['location'] else None, 
                    'imagen': personaje_api['image'],
                    'URL': personaje_api['url'],
                })
                personaje = personaje_api 
                
        except requests.exceptions.RequestException as e:
            print(f"Error al buscar el personaje: {e}")

    if request.method == 'POST':
        form = PersonajesForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista_personajes')  
    return render(request, 'personajes/form_personaje.html', {'form': form, 'personaje': personaje})

def editar_personaje(request, id):
    personaje = get_object_or_404(personajes, id=id)
    if request.method == 'POST':
        form = PersonajesForm(request.POST, instance=personaje)
        if form.is_valid():
            form.save() 
            return redirect('detalle_personaje', id=personaje.id)
    else:
        form = PersonajesForm(instance=personaje)
    return render(request, 'personajes/editar_personaje.html', {'form': form, 'personaje': personaje})

def eliminar_personaje(request, id):
    personaje = get_object_or_404(personajes, id=id)
    if request.method == 'POST':
        personaje.delete()
        return redirect('lista_personajes')
    return render(request, 'personajes/confirmar_eliminacion.html', {'personaje': personaje})