from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Ejercicio
from .forms import RegistrarEntrenamiento, AnadirEjercicioPersonalizado
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def principal(request):
    return render(request, 'gymApp/principal.html')

class RegistroUsuario(CreateView):
    template_name = 'registration/registroUsuario.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('principal')

class RegistrarEntreno(LoginRequiredMixin, CreateView):
    template_name = 'gymApp/registrarEntreno.html'
    form_class = RegistrarEntrenamiento
    success_url = reverse_lazy('registrarEntreno')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class AnadirEjercicio(LoginRequiredMixin, View):
    template_name = 'gymApp/anadirEjercicio.html'
    model = Ejercicio
    
    def get(self, request):
        form = AnadirEjercicioPersonalizado()
        ejercicios = Ejercicio.objects.all()
        return render(request, self.template_name, {'form': form, 'ejercicios': ejercicios})

    def post(self, request):
        accion = request.POST['accion']
        existeEjercicio = False
        form = AnadirEjercicioPersonalizado(request.POST)

        if accion == 'crear' and form.is_valid():
            existeEjercicio = Ejercicio.objects.filter(nombre=form.cleaned_data['nombre']).exists()

            if not existeEjercicio:
                form.save()
                return redirect('anadirEjercicio')
            
        elif accion == 'eliminar':
            ejercicioId = request.POST['ejercicio_id']

            if ejercicioId:
                Ejercicio.objects.filter(id=ejercicioId).delete()
                return redirect('anadirEjercicio')

        ejercicios = Ejercicio.objects.all()
        return render(request, self.template_name, {'form': form, 'ejercicios': ejercicios, 'existeEjercicio': existeEjercicio})
