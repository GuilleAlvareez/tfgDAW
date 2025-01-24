# Generated by Django 5.1.3 on 2025-01-24 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0005_alter_entreno_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreno',
            name='numero_ejercicios',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entreno',
            name='comentarios',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='entreno',
            name='ejercicios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymApp.ejercicio'),
        ),
    ]
