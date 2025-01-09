# Generated by Django 5.1.3 on 2025-01-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0002_ejercicio_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejercicio',
            name='dia',
        ),
        migrations.AddField(
            model_name='dia',
            name='ejercicios',
            field=models.ManyToManyField(to='gymApp.ejercicio'),
        ),
        migrations.AlterField(
            model_name='bloque',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
