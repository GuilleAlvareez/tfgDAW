from django import forms
from django.forms import formset_factory, modelformset_factory
from .models import Entreno, Ejercicio, Ejercicio_realizado

class anadirEjercicioRealizado(forms.ModelForm):
    class Meta: 
        model = Ejercicio_realizado
        fields = ['nombre', 'peso', 'series', 'repeticiones', 'observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={
                'placeholder': 'Añade tus observaciones del ejercicio',
                'style': 'resize:none;',
                'class': 'textarea',
            }),
        }

EjercicioRealizadoFormSet = modelformset_factory(Ejercicio_realizado, anadirEjercicioRealizado)


class RegistrarEntrenamiento(forms.ModelForm):
    class Meta:
        model = Entreno
        fields = ['nombre', 'fecha', 'valoracion', 'numero_ejercicios', 'comentarios']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre del entreno'
            }),
            'fecha': forms.DateInput(attrs={
                'type': 'date'
            }),
            'valoracion': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'placeholder': 'Valoración del 1 al 5'
            }),
            'comentarios': forms.Textarea(attrs={
                'placeholder': 'Añade tus comentarios',
                'style': 'resize:none;'
            }),
        }

class AnadirEjercicioPersonalizado(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = ['nombre', 'musculos']
