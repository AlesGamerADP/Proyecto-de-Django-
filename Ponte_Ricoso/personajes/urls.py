from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_personajes, name='lista_personajes'),
    path('detalle/<int:id>/', views.detalle_personaje, name='detalle_personaje'),
    path('crear/', views.crear_personaje, name='crear_personaje'),
    path('editar/<int:id>/', views.editar_personaje, name='editar_personaje'),
    path('eliminar/<int:id>/', views.eliminar_personaje, name='eliminar_personaje'),
    
]
