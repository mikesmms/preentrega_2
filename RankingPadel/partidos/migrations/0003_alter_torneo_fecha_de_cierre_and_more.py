# Generated by Django 5.0.6 on 2024-05-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partidos', '0002_alter_jugador_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='fecha_de_cierre',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='fecha_de_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
