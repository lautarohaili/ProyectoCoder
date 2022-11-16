from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

  path('', views.mostrar_home, name='Home' ),
  path('mostrar_contacto/', views.mostrar_contacto, name='Contacto'),
  path('crear_post/', views.crear_post, name='Crear'),
  path('buscar_post', views.buscar_post, name='Buscar'),
  path('mostrar_post', views.mostrar_post, name='Mostrar'),

]