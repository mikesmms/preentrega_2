from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomCreationForm
from django.http import HttpRequest
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"

    def get_success_url(self):
        return reverse_lazy("Partidos:index")

def register(request: HttpRequest):
    if request.method == "POST":
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "core/index.html", {"mensaje": f"Usuario {username} creado con exito"})
    else:
        form = CustomCreationForm()
    return render(request, "core/register.html", {"form": form})