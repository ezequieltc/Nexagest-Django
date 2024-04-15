from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Venta, Cliente

# Create your views here.

@login_required
def index(request):
    return render(request, 'main.html')
@login_required
def cerrarSesion(request):
    logout(request)
    return redirect(reverse('login:login'))

@login_required
def ventasVista(request):
    ventas = Venta.objects.all().order_by("-fecha_venta")
    for venta in ventas:
        print(venta.fecha_venta)
    return render(request, 'ventas.html', {"ventas":ventas})