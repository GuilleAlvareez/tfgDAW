from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Ejercicio, Ejercicio_realizado, Entreno, Musculo
from .forms import EjercicioRealizadoFormSet, RegistrarEntrenamiento, AnadirEjercicioPersonalizado, anadirEjercicioRealizado
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def principal(request):
    return render(request, 'gymApp/principal.html')

class RegistroUsuario(CreateView):
    template_name = 'registration/registroUsuario.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('principal')

class AnadirEjercicio(LoginRequiredMixin, CreateView):
    model = Ejercicio
    template_name = 'gymApp/anadirEjercicio.html'
    form_class = AnadirEjercicioPersonalizado
    context_object_name = 'ejercicios'
    success_url = reverse_lazy('anadirEjercicio')

    def form_valid(self, form):
        ejercicio = form.save(commit=False)

        ejercicio.visibilidad = self.request.user.username
        ejercicio.save()
        messages.success(self.request, 'Ejercicio creado')
        
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        musculos = Musculo.objects.all()
        
        ejercicios = self.get_queryset()

        paginator = Paginator(ejercicios, 5)
        page = self.request.GET.get('page')
        ejerciciosMostar = paginator.get_page(page)

        contexto['ejerciciosMostar'] = ejerciciosMostar
        contexto['musculos'] = musculos

        return contexto

    def get_queryset(self):
        query = super().get_queryset()
        usuario = self.request.user
        musculoAFiltrar = self.request.GET.get('filtroMusculo')

        if musculoAFiltrar:
            query = query.filter(Q(musculos__nombre=musculoAFiltrar) & Q(Q(visibilidad=usuario.username) | Q(visibilidad='all')))
        else:
            query = query.filter(Q(visibilidad='all') | Q(visibilidad=usuario.username))

        return query
    
    
class BorrarEjercicio(DeleteView):
    model = Ejercicio
    template_name = 'gymApp/borrarEjercicio.html'
    success_url = reverse_lazy('anadirEjercicio')

class RegistrarEntreno(LoginRequiredMixin, CreateView):
    model = Entreno
    template_name = 'gymApp/registrarEntreno.html'
    form_class = RegistrarEntrenamiento
    success_url = reverse_lazy('registrarEntreno')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        ejerciciosRealizados = Ejercicio_realizado.objects.all()

        contexto['entrenos'] = Entreno.objects.all()
        contexto['ejerciciosRealizados'] = ejerciciosRealizados

        return contexto

class EditarEntreno(LoginRequiredMixin, UpdateView):
    model = Entreno
    template_name = 'gymApp/editarEntreno.html'
    form_class = RegistrarEntrenamiento
    success_url = reverse_lazy('registrarEntreno')

class AnadirEjercicioRealizado(CreateView):
    model = Ejercicio_realizado
    template_name = 'gymApp/anadirEjercicioRealizado.html'
    form_class = anadirEjercicioRealizado

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        entreno = Entreno.objects.get(id=self.kwargs['pk'])
        
        EjercicioRealizadoFormSet = modelformset_factory(Ejercicio_realizado, form=anadirEjercicioRealizado, extra=entreno.numero_ejercicios, fields=['nombre', 'peso', 'series', 'repeticiones', 'observaciones'])

        contexto['formset'] = EjercicioRealizadoFormSet(queryset=Ejercicio_realizado.objects.none())

        return contexto

    def post(self, request, *args, **kwargs):
        formset = EjercicioRealizadoFormSet(request.POST)

        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        formularios = formset.save(commit=False)
        entreno = Entreno.objects.get(id=self.kwargs['pk'])
        
        for formulario in formularios:
            formulario.entreno = entreno
            formulario.save()

        return redirect('registrarEntreno')

class ListaEjerciciosDeUnEntreno(ListView):
    model = Ejercicio_realizado
    template_name = 'gymApp/listaEjerciciosDeUnEntreno.html'
    context_object_name = 'ejerciciosRealizados'

    def get_queryset(self):
        query = super().get_queryset()
        entreno = Entreno.objects.get(id=self.kwargs['pk'])

        query = query.filter(entreno=entreno)

        return query
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto['entreno'] = Entreno.objects.get(id=self.kwargs['pk'])
        
        return contexto

class BorrarEntreno(DeleteView):
    model = Entreno
    template_name = 'gymApp/borrarEntreno.html'
    success_url = reverse_lazy('registrarEntreno')
