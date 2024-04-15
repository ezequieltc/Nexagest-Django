from django.urls import path
from . import views
app_name = "login"

urlpatterns = [
    path("", views.loginPagina, name="login"),
    path("newuser", views.crearUsuario, name="crearUsuario"),
]
