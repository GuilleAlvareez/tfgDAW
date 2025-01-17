from django import forms
from .models import Entreno, Ejercicio

class RegistrarEntrenamiento(forms.ModelForm):
    class Meta:
        model = Entreno
        fields = ['fecha', 'ejercicios', 'valoracion', 'comentarios']
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