from django import forms
from django.forms import formset_factory
from .models import Entreno, Ejercicio, Ejercicio_realizado

class anadirEjercicioRealizado(forms.ModelForm):
    class Meta: 
        model = Ejercicio_realizado
        fields = '__all__'
        widgets = {
            'observaciones': forms.Textarea(attrs={
                'placeholder': 'Añade tus observaciones del ejercicio',
                'style': 'resize:none;'
            }),
        }

EjercicioRealizadoFormSet = formset_factory(anadirEjercicioRealizado)


class RegistrarEntrenamiento(forms.ModelForm):
    class Meta:
        model = Entreno
        fields = ['fecha', 'valoracion', 'comentarios']
        widgets = {
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
        fields = '__all__'
