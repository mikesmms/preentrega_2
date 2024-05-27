from django.urls import path
from . import views

from core.views import CustomLoginView

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
]
