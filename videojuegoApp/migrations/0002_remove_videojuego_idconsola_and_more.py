# Generated by Django 4.1.2 on 2022-12-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videojuegoApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videojuego',
            name='idConsola',
        ),
        migrations.AddField(
            model_name='videojuego',
            name='consolaCompatible',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='cantidadJugadores',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='duracion',
            field=models.CharField(max_length=15),
        ),
    ]
