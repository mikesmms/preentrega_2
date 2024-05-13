from django.urls import path
from . import views

app_name = "Partidos"

urlpatterns = [
    path("", views.index, name="index"),
]
