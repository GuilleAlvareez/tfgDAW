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

class AñadirEjercicio(LoginRequiredMixin, View):
    template_name = 'gymApp/añadirEjercicio.html'

    def get(self, request):
        form = AñadirEjercicioPersonalizado()
        ejercicios = Ejercicio.objects.all()
        return render(request, self.template_name, {'form': form, 'ejercicios': ejercicios})

    def post(self, request):
        accion = request.POST['accion']
        existeEjercicio = False
        form = AñadirEjercicioPersonalizado(request.POST)

        if accion == 'crear' and form.is_valid():
            existeEjercicio = Ejercicio.objects.filter(nombre=form.cleaned_data['nombre']).exists()

            if not existeEjercicio:
                form.save()
                return redirect('añadirEjercicio')
            
        elif accion == 'eliminar':
            ejercicio_id = request.POST['ejercicio_id']

            if ejercicio_id:
                Ejercicio.objects.filter(id=ejercicio_id).delete()
                return redirect('añadirEjercicio')

        ejercicios = Ejercicio.objects.all()
        return render(request, self.template_name, {'form': form, 'ejercicios': ejercicios, 'existeEjercicio': existeEjercicio})
