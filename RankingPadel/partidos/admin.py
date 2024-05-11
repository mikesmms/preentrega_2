from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Jugador)
admin.site.register(models.Torneo)
admin.site.register(models.Partido)