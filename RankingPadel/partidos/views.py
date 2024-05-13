from django.shortcuts import render

# Create your views here.
from . import models

def index(request):
    consulta = models.Partido.objects.all()
    contexto = {"partidos": consulta}
    return render(request, "partidos/index.html", contexto)