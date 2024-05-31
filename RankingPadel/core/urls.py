from django.urls import path
from . import views

from core.views import CustomLoginView, register
from django.contrib.auth.views import LogoutView

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", register, name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
]
