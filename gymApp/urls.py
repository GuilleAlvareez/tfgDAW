from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('registrarEntreno', RegistrarEntreno.as_view(), name='registrarEntreno'),
    path('añadirEjercicio', AñadirEjercicio.as_view(), name='añadirEjercicio')
]
