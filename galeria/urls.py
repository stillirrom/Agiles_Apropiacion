from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views



urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('<str:tipo>/<int:idbd>',views.detalle,name='detalleGal')

]
=======
    path('agregarUsuario/', views.agregar_usuario, name='agregarUsuario'),
    path('registrarUsuario/', views.registrar_usuario, name='registrarUsuario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 0b0a96948b6e83df26bd9ccd6824cee1e25ba1e4
