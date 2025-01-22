from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Ejercicio
from .forms import RegistrarEntrenamiento, AnadirEjercicioPersonalizado
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EjercicioRealizadoFormSet
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['formset'] = EjercicioRealizadoFormSet(self.request.POST)
        else:
            context['formset'] = EjercicioRealizadoFormSet()
            
        return context

class AnadirEjercicio(LoginRequiredMixin, CreateView):
    template_name = 'gymApp/anadirEjercicio.html'
    form_class = AnadirEjercicioPersonalizado
    context_object_name = 'ejercicios'
    success_url = reverse_lazy('anadirEjercicio')
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto['ejercicios'] = Ejercicio.objects.filter(visibilidad='all')

        return contexto
    
class BorrarEjercicio(DeleteView):
    model = Ejercicio
    template_name = 'gymApp/borrarEjercicio.html'
    success_url = reverse_lazy('anadirEjercicio')