from django.db import models
from django.contrib.auth.models import User
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

class Entreno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    valoracion = models.IntegerField()
    ejercicios = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    comentarios = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Entreno'
        verbose_name_plural = 'Entrenos'

    def __str__(self):
        return f"{self.fecha}"


class Ejercicio_realizado(models.Model):
    entreno = models.ForeignKey(Entreno, on_delete=models.CASCADE)
    nombre = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    peso = models.IntegerField()
    series = models.IntegerField()
    repeticiones = models.IntegerField()
    observaciones = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Ejercicio_realizado'
        verbose_name_plural = 'Ejercicios_realizados'

    def __str__(self):
        return f"{self.peso}kg {self.series}x{self.repeticiones}"
