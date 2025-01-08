from django.shortcuts import render
from django.views.generic import ListView
from .models import Bloque
# Create your views here.

def principal(request):
    return render(request, 'gymApp/principal.html')

class Bloques(ListView):
    model = Bloque
    template_name = 'gymApp/bloques.html'
    context_object_name = 'listaBloques'