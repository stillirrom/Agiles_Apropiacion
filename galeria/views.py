<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Imagen, Audio, Video
from django.conf import settings
=======
from django.shortcuts import render
from .models import Imagen, Audio, Video
import json
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
>>>>>>> 0b0a96948b6e83df26bd9ccd6824cee1e25ba1e4

# Create your views here.


def index(request):
    lstImagen = Imagen.objects.all()
    lstAudio = Audio.objects.all()
    lstVideo = Video.objects.all()
    print('*********************************************************')
    print(lstImagen)
    return render(request, 'lista_galeria.html', context={'lstImagen': lstImagen, 'lstAudio': lstAudio, 'lstVideo': lstVideo})


<<<<<<< HEAD
def detalle(request, tipo, idbd):
    if tipo==settings.IMAGEN:
        multimedia=get_object_or_404(Imagen,id=idbd)
        imagenUrl=multimedia.contenido.url
        print('contenido')
        print(multimedia.contenido)

    if tipo==settings.VIDEO:
        multimedia=get_object_or_404(Video,id=idbd)

    if tipo==settings.AUDIO:
        multimedia=get_object_or_404(Audio,id=idbd)
        audioUrl=multimedia.contenido.url

    titulo=multimedia.titulo
    autor=multimedia.autor
    fecha_creacion=multimedia.fecha_creacion.strftime("%d/%m/%Y %H:%M")
    categoria=multimedia.categoria
    usuario=multimedia.usuario
    ciudad=multimedia.ciudad
    pais=multimedia.pais

    context={'tipo':tipo,'titulo':titulo,'autor':autor,'fecha_creacion':fecha_creacion,'categoria':categoria,
             'usuario':usuario,'ciudad':ciudad,'pais':pais,'imagenUrl':imagenUrl,'audioUrl':audioUrl}

    return render(request, 'detalle.html',context)
=======
@csrf_exempt
def registrar_usuario(request):
    return render(request, 'registrarUsuario.html')


@csrf_exempt
def agregar_usuario(request):
    if request.method == 'POST':
        jsonUser = json.load(request)
        nombre_usuario = jsonUser['nombre_usuario']
        nombre = jsonUser['nombre']
        apellido = jsonUser['apellido']
        contraseña = jsonUser['contraseña']
        correo_electronico = jsonUser['correo_electronico']

        user_model = User.objects.create_user(username=nombre_usuario, password=contraseña)
        user_model.first_name = nombre
        user_model.last_name = apellido
        user_model.email = correo_electronico
        user_model.save()
    return HttpResponse(serializers.serialize('json', [user_model]))
>>>>>>> 0b0a96948b6e83df26bd9ccd6824cee1e25ba1e4
