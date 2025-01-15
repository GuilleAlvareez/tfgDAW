from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Ejercicio
from .forms import RegistrarEntrenamiento, AñadirEjercicioPersonalizado
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def principal(request):
    return render(request, 'gymApp/principal.html')

class RegistrarEntreno(CreateView):
    template_name = 'gymApp/registrarEntreno.html'
    form_class = RegistrarEntrenamiento

class AñadirEjercicio(View):
    template_name = 'gymApp/añadirEjercicio.html'

    def get(self, request):
        form = AñadirEjercicioPersonalizado()
        ejercicios = Ejercicio.objects.all()
        return render(request, self.template_name, {'form': form, 'ejercicios': ejercicios, })
    
    def post(self, request):
        form = AñadirEjercicioPersonalizado(request.POST)
        if form.is_valid():
            existeEjercicio =  Ejercicio.objects.filter(nombre = form.cleaned_data['nombre']).exists()
            
            if not existeEjercicio:
                form.save()
                return redirect('añadirEjercicio')
        ejercicios = Ejercicio.objects.all()
        return render(request, self.template_name, {'form': form, 'ejercicios': ejercicios, 'existeEjercicio': existeEjercicio})