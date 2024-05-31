from django.urls import path
from . import views
from partidos.views import JugadoresDetail

app_name = "Partidos"

urlpatterns = [
    path("index", views.index, name="index"),
    path("partidos_list", views.partidos_list, name="partidos_list"),
    path("partidos_create", views.partidos_create , name="partidos_create"),
    path('partidos/<int:pk>/delete/', views.PartidoDelete.as_view(), name='partido_delete'),
    path("jugadores_list", views.jugadores_list, name = "jugadores_list"),
    path("jugadores_create", views.jugadores_create, name = "jugadores_create"),
    path("torneos_list", views.torneos_list, name = "torneos_list"),
    path("torneos_create", views.torneos_create, name = "torneos_create"),
    path("jugador/detail/<int:pk>", JugadoresDetail.as_view(), name = "jugador_detail"),

]
