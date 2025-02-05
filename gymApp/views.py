from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Ejercicio, Ejercicio_realizado, Entreno
from .forms import RegistrarEntrenamiento, AnadirEjercicioPersonalizado, anadirEjercicioRealizado
from django.views.generic import CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EjercicioRealizadoFormSet
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404


# Create your views here.

def principal(request):
    return render(request, 'gymApp/principal.html')

class RegistroUsuario(CreateView):
    template_name = 'registration/registroUsuario.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('principal')

class AnadirEjercicio(LoginRequiredMixin, CreateView):
    template_name = 'gymApp/anadirEjercicio.html'
    form_class = AnadirEjercicioPersonalizado
    context_object_name = 'ejercicios'
    success_url = reverse_lazy('anadirEjercicio')

    def form_valid(self, form):
        messages.success(self.request, 'Ejercicio creado')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto['ejercicios'] = Ejercicio.objects.filter(visibilidad='all')

        return contexto
    
class BorrarEjercicio(DeleteView):
    model = Ejercicio
    template_name = 'gymApp/borrarEjercicio.html'
    success_url = reverse_lazy('anadirEjercicio')

class RegistrarEntreno(LoginRequiredMixin, CreateView):
    template_name = 'gymApp/registrarEntreno.html'
    form_class = RegistrarEntrenamiento
    success_url = reverse_lazy('registrarEntreno')

    def form_valid(self, form):
        # Asignamos el usuario logueado al campo 'usuario'
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto['entrenos'] = Entreno.objects.all()

        return contexto

def AnadirEjercicioRealizado(request, pk):
    entreno = get_object_or_404(Entreno, pk=pk)

    EjercicioRealizadoFormSet = modelformset_factory(Ejercicio_realizado, form=anadirEjercicioRealizado, extra=entreno.numero_ejercicios, fields=['nombre', 'peso', 'series', 'repeticiones', 'observaciones'])

    queryset = Ejercicio_realizado.objects.filter(entreno = entreno)

    if request.method == 'POST':
        formset = EjercicioRealizadoFormSet(request.POST, queryset=queryset)

        if formset.is_valid():
            ejercicios = formset.save(commit=False)
            for ejercicio in ejercicios:
                ejercicio.entreno = entreno
                ejercicio.save()
            return redirect('registrarEntreno')
    else:
        formset = EjercicioRealizadoFormSet(queryset=queryset)
    return render(request, 'gymApp/anadirEjercicioRealizado.html', { 'formset': formset, 'numEjercicios': entreno.numero_ejercicios })




# class AnadirEjercicioRealizado(FormView):
#     model = Ejercicio_realizado
#     template_name = 'gymApp/anadirEjercicioRealizado.html'
#     success_url = reverse_lazy('registrarEntreno')

#     def get_context_data(self, **kwargs):
#         contexto = super().get_context_data(**kwargs)

#         entrenoId = self.kwargs['pk']
#         entreno = Entreno.objects.get(id=entrenoId)

#         EjercicioRealizadoFormSet = formset_factory(anadirEjercicioRealizado, extra=entreno.numero_ejercicios)

#         contexto['formset'] = EjercicioRealizadoFormSet
#         contexto['numEjercicios'] = entreno.numero_ejercicios
        
#         return contexto
    
#     # def form_valid(self, form):
#     #     entreno = Entreno.objects.get(id=self.kwargs['pk'])
        
#     #     for f in form:
#     #         if f.cleaned_data:
#     #             ejercicio_realizado = f.save(commit=False)
#     #             ejercicio_realizado.entreno = entreno
#     #             ejercicio_realizado.save()
#     #             entreno.ejercicios.add(ejercicio_realizado)
        
#     #     return super().form_valid(form)