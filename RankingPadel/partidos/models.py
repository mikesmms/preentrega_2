from django.db import models

# Create your models here.

class Jugador(models.Model):
    OPCIONES_DE_GENERO = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('Otro', 'Otro'),
    ]
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=6, choices= OPCIONES_DE_GENERO)
    nacimiento = models.DateField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
class Torneo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_de_inicio = models.DateField()
    fecha_de_cierre = models.DateField()
    
class Partido(models.Model):
    jugador_local_1 = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, blank=True)
    jugador_local_2 = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, blank=True)
    games_local = models.PositiveIntegerField()
    games_visitante = models.PositiveIntegerField()
    jugador_visitante_1 = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, blank=True)
    jugador_visitante_2 = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_de_partido = models.DateTimeField()
    torneo = models.ForeignKey(Torneo, on_delete=models.SET_NULL, null=True, blank=True)