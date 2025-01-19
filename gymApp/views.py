from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Ejercicio
from .forms import RegistrarEntrenamiento, AñadirEjercicioPersonalizado
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def principal(request):
    return render(request, 'gymApp/principal.html')

class RegistroUsuario(CreateView):
    template_name = 'registration/registroUsuario.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('principal')

class RegistrarEntreno(CreateView):
    template_name = 'gymApp/registrarEntreno.html'
    form_class = RegistrarEntrenamiento

class AñadirEjercicio(LoginRequiredMixin, CreateView):
    template_name = 'gymApp/añadirEjercicio.html'
    form_class = AñadirEjercicioPersonalizado
    context_object_name = 'ejercicios'
    success_url = reverse_lazy('añadirEjercicio')
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto['ejercicios'] = Ejercicio.objects.filter(visibilidad='all')

        return contexto