# Generated by Django 5.1.3 on 2025-02-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0007_remove_entreno_ejercicios_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreno',
            name='nombre',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
