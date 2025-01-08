from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('bloques', Bloques.as_view(), name='bloques')
]
