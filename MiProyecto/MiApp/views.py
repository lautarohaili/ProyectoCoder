from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import CrearPostForm, ContactoForm

def mostrar_home (request):
    return render(request, "MiApp/home.html")

def mostrar_contacto(request):
    return render(request, "MiApp/contacto.html")


def crear_consulta(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            contacto = Contacto(nombre=formulario_limpio["nombre"], email=formulario_limpio["email"], consulta=formulario_limpio["consulta"])

            contacto.save()

            return render(request, "MiApp/home.html")
    else:
        formulario = ContactoForm()
        
    return render(request, "MiApp/contacto.html", {"formulario": formulario})

def crear_post(request):
    if request.method == 'POST':

        formulario = CrearPostForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            post = Post(titulo=formulario_limpio['titulo'], fecha=formulario_limpio['fecha'], texto=formulario_limpio['texto'])

            post.save()

            return render(request, "MiApp/home.html")
    else:
        formulario = CrearPostForm()
        
    return render(request, "MiApp/crear_post.html", {"formulario": formulario})

def buscar_post(request):

    if request.GET.get('titulo', False): # -> 12345
        titulo = request.GET['titulo']
        posts = Post.objects.filter(titulo__icontains=titulo)

        return render(request, 'MiApp/home.html', {'posts': posts, 'titulo': titulo})
    else:
        respuesta = 'No existe el post solicitado'
    return render(request, 'MiApp/buscar_post.html', {'respuesta': respuesta})


def mostrar_post (request):

    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'MiApp/mostrar_post.html', context=context)

