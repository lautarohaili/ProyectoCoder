from django.contrib import admin
from django.urls import path
from .views import mostrar_home, mostrar_contacto, crear_post, buscar_post

urlpatterns = [

  path('', mostrar_home, name='Home' ),
  path('mostrar_contacto/', mostrar_contacto, name='Contacto'),
  path('crear_post/', crear_post, name='Crear'),
  path('buscar_post', buscar_post, name='Buscar'),

]