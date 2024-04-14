from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, request
from django.contrib import messages
from .models import Usuarios
from django.db import IntegrityError

def login(request):
    if request.method == 'POST':
        # Acceder a los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Realizar la verificación aquí (por ejemplo, autenticar al usuario)
        userBase = Usuarios.objects.filter(usuario = username, contrasena = password)
        if userBase.exists():
            print("Joya")
            return redirect(reverse('main:main'))
        else:
            # Si la verificación falla, puedes mostrar un mensaje de error o volver a renderizar el formulario
            messages.error(request, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')

    # Si la solicitud es GET o la verificación falla, renderiza la plantilla del formulario de inicio de sesión
    return render(request, 'login.html')


def crearUsuario(request):
    if request.method == 'POST':
        nombre = request.POST.get("name")
        apellido = request.POST.get("surname")
        email = request.POST.get("email")
        usuario = request.POST.get("user")
        contrasena = request.POST.get("password")
        try:
            Usuarios.objects.create(
                nombre = nombre,
                apellido = apellido,
                email = email,
                usuario = usuario,
                contrasena = contrasena
            )
            messages.success(request, "Usuario creado exitosamente")
        except IntegrityError:
            messages.error(request, "El usuario ya existe en la base de datos")

    print(request)
    return render(request, "crearUsuario.html")

