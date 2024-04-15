from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index" ),
    path("cerrarsesion", views.cerrarSesion, name="cerrarSesion"),
    path("ventas", views.ventasVista, name="ventasVista")
]