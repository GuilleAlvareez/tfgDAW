from django import forms
from .models import Entreno, Ejercicio

class RegistrarEntrenamiento(forms.ModelForm):
    class Meta:
        model = Entreno
        fields = ['fecha', 'valoracion', 'comentarios']

class AñadirEjercicio(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = '__all__'