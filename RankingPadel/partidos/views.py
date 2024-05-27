from django.shortcuts import render, redirect
from django.db.models import Q
from partidos.forms import PartidoForm, JugadorForm, TorneoForm
from partidos.models import Partido, Jugador
from django.views.generic import DetailView


# Create your views here.
from . import models

def index(request):
    consulta = models.Partido.objects.all()
    contexto = {"partidos": consulta}
    return render(request, "partidos/index.html", contexto)


def partidos_list(request):
    busqueda = request.GET.get("busqueda", "")
    partidos = Partido.objects.all() 
    if busqueda:
        partidos = Partido.objects.filter(
            Q(jugador_local_1__nombre__icontains=busqueda) | 
            Q(jugador_local_1__apellido__icontains=busqueda) |
            Q(jugador_local_2__nombre__icontains=busqueda) | 
            Q(jugador_local_2__apellido__icontains=busqueda) |
            Q(jugador_visitante_1__nombre__icontains=busqueda) |
            Q(jugador_visitante_1__apellido__icontains=busqueda) |
            Q(jugador_visitante_2__nombre__icontains=busqueda) |
            Q(jugador_visitante_2__apellido__icontains=busqueda)
        )
    context = {'partidos': partidos, 'busqueda': busqueda}
    return render(request, "partidos/partidos_list.html", context)

def partidos_create(request):
    if request.method == "POST":
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Partidos:partidos_list")
    else: #GET
        form = PartidoForm()
    return render(request, "partidos/partidos_create.html", {"form": form})


def jugadores_list(request):
    consulta = models.Jugador.objects.all()
    contexto = {"jugadores": consulta}
    return render(request, "partidos/jugadores_list.html", contexto)

class JugadoresDetail(DetailView):
    model = Jugador

def jugadores_create(request):
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Partidos:jugadores_list")
    else: #GET
        form = JugadorForm()
    return render(request, "partidos/jugadores_create.html", {"form": form})


def torneos_list(request):
    consulta = models.Torneo.objects.all()
    contexto = {"torneos": consulta}
    return render(request, "partidos/torneos_list.html", contexto)

def torneos_create(request):
    if request.method == "POST":
        form = TorneoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Partidos:torneos_list")
    else: #GET
        form = TorneoForm()
    return render(request, "partidos/torneos_create.html", {"form": form})