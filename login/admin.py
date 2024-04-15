from django.contrib import admin
from .models import Usuario

# Register your models here.

class Usuarios_Admin(admin.ModelAdmin):
    list_display= ("id", "nombre" , "apellido" ,"usuario", "contrasena","email","admin")

admin.site.register(Usuario, Usuarios_Admin)
