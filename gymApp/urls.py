from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('borrarEjercicio/<int:pk>', BorrarEjercicio.as_view(), name='borrarEjercicio'),
    path('anadirEjercicio', AnadirEjercicio.as_view(), name='anadirEjercicio'),

    path('registro', RegistroUsuario.as_view(), name='registroUsuario'),

    path('registrarEntreno', RegistrarEntreno.as_view(), name='registrarEntreno'),
    path('registrarEntreno/<int:pk>/editar', EditarEntreno.as_view(), name='editarEntreno'),
    # path('registrarEntreno/<int:pk>/anadirEjercicioRealizado', AnadirEjercicioRealizado.as_view(), name='anadirEjercicioRealizado'),
    # path('registrarEntreno/<int:pk>/anadirEjercicioRealizado', AnadirEjercicioRealizado, name='anadirEjercicioRealizado'),
    path('registrarEntreno/<int:pk>/anadirEjercicioRealizado', AnadirEjercicioRealizado.as_view(), name='anadirEjercicioRealizado'),
    path('registrarEntreno/<int:pk>/listaEjercicios', ListaEjerciciosDeUnEntreno.as_view(), name='listaEjerciciosDeUnEntreno'),
    path('borrarEntreno/<int:pk>', BorrarEntreno.as_view(), name='borrarEntreno'),
]
