from django.contrib import admin

# Register your models here.

from . import models

class PartidoAdmin(admin.ModelAdmin):
    list_display = ("jugador_local_1",
                    "jugador_local_2",
                    "games_local",
                    "games_visitante",
                    "jugador_visitante_1",
                    "jugador_visitante_2",
                    "fecha_de_partido",
                    "torneo")
    list_display_links = ("jugador_local_1", "jugador_local_2", "jugador_visitante_1","jugador_visitante_2","torneo",)
    list_filter = ("torneo",)
    date_hierarchy = "fecha_de_partido"

admin.site.register(models.Jugador)
admin.site.register(models.Torneo)
admin.site.register(models.Partido, PartidoAdmin)