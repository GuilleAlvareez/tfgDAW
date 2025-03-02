from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
# Create your models here.

class Musculo(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Musculo'
        verbose_name_plural = 'Musculos'

    def __str__(self):
        return f"{self.nombre}"

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    musculos = models.ManyToManyField(Musculo)
    visibilidad = models.CharField(max_length=200, default='all')

    class Meta:
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'

    def __str__(self):
        return f"{self.nombre}"
    
    def clean(self):
        if Ejercicio.objects.filter(nombre=self.nombre).exists():
            raise ValidationError('El ejercicio ya existe')
        return super().clean()

class Entreno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    valoracion = models.IntegerField()
    numero_ejercicios = models.IntegerField()
    comentarios = models.CharField(max_length=300, null=True)
    
    class Meta:
        verbose_name = 'Entreno'
        verbose_name_plural = 'Entrenos'

    def __str__(self):
        return f"{self.fecha}"


class Ejercicio_realizado(models.Model):
    entreno = models.ForeignKey(Entreno, on_delete=models.CASCADE, related_name='ejercicios')
    nombre = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    peso = models.IntegerField()
    series = models.IntegerField()
    repeticiones = models.IntegerField()
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Ejercicio_realizado'
        verbose_name_plural = 'Ejercicios_realizados'

    def __str__(self):
        return f"{self.peso}kg {self.series}x{self.repeticiones}"
