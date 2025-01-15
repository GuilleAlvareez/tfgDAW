# Generated by Django 5.1.3 on 2025-01-15 11:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0003_remove_ejercicio_dia_dia_ejercicios_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Musculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Musculo',
                'verbose_name_plural': 'Musculos',
            },
        ),
        migrations.RemoveField(
            model_name='semana',
            name='bloque',
        ),
        migrations.RemoveField(
            model_name='dia',
            name='ejercicios',
        ),
        migrations.RemoveField(
            model_name='dia',
            name='semana',
        ),
        migrations.RemoveField(
            model_name='ejercicio',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='ejercicio',
            name='peso',
        ),
        migrations.RemoveField(
            model_name='ejercicio',
            name='repeticiones',
        ),
        migrations.RemoveField(
            model_name='ejercicio',
            name='series',
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='visibilidad',
            field=models.CharField(default='all', max_length=200),
        ),
        migrations.CreateModel(
            name='Entreno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('valoracion', models.IntegerField()),
                ('comentarios', models.CharField(max_length=300)),
                ('ejercicios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymApp.ejercicio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entreno',
                'verbose_name_plural': 'Entrenos',
            },
        ),
        migrations.CreateModel(
            name='Ejercicio_realizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.IntegerField()),
                ('series', models.IntegerField()),
                ('repeticiones', models.IntegerField()),
                ('observaciones', models.CharField(max_length=200)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymApp.ejercicio')),
                ('entreno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymApp.entreno')),
            ],
            options={
                'verbose_name': 'Ejercicio_realizado',
                'verbose_name_plural': 'Ejercicios_realizados',
            },
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='musculos',
            field=models.ManyToManyField(to='gymApp.musculo'),
        ),
        migrations.DeleteModel(
            name='Bloque',
        ),
        migrations.DeleteModel(
            name='Dia',
        ),
        migrations.DeleteModel(
            name='Semana',
        ),
    ]
