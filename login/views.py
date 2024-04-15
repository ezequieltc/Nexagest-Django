from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, request
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def loginPagina(request):
    if request.user.is_authenticated:
        return redirect(reverse('main:index'))
    if User.objects.filter(is_superuser = True).exists() == False:
        print("No hay super usuario")       
        User.objects.create_superuser("admin","","admin")

    if request.method == 'POST':
        # Acceder a los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Realizar la verificación aquí (por ejemplo, autenticar al usuario)
        user = authenticate(request, username = username, password = password)
        if user is not None:
            print("Joya")
            login(request, user)
            return redirect(reverse('main:index'))
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
            user = User.objects.create_user(usuario,email,contrasena)
            user.first_name = nombre
            user.last_name = apellido
            user.save()
            messages.success(request, "Usuario creado exitosamente, redirigiendo en 3 segundos...")
        except:
            messages.error(request, "El usuario ya existe en la base de datos")

    print(request)
    return render(request, "crearUsuario.html")


