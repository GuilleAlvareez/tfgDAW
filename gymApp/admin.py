from django.contrib import admin
from .models import Entreno, Musculo, Ejercicio, Ejercicio_realizado

# Register your models here.
admin.site.register(Entreno)
admin.site.register(Ejercicio_realizado)
admin.site.register(Musculo)
admin.site.register(Ejercicio)