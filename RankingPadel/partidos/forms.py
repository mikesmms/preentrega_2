from django import forms

from . import models

class  JugadorForm(forms.ModelForm):
    class Meta:
        model = models.Jugador
        fields = ["nombre", 'apellido']


class  TorneoForm(forms.ModelForm):
    class Meta:
        model = models.Torneo
        fields = ["nombre"]

class  PartidoForm(forms.ModelForm):
    class Meta:
        model = models.Partido
        fields = ["fecha_de_partido", "jugador_local_1", "jugador_local_2", "games_local",  "games_visitante", "jugador_visitante_1", "jugador_visitante_2"]