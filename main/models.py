from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.

class Contacto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100, default="", verbose_name="Nombre")
    apellido = models.CharField(max_length=100,default="", verbose_name="Apellido")
    email = models.EmailField(max_length=100,default="", verbose_name="Email")
    telefono = models.CharField(max_length= 15,default="", blank=True)
    direccion = models.CharField(max_length=100,default="")


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombreCliente = models.CharField(max_length= 100,default="", verbose_name="Cliente")
    is_empresa = models.BooleanField(default= False, verbose_name="Es Empresa")
    contactos = models.ManyToManyField(Contacto)




class Venta(models.Model):
    ESTADOS = {"En Proceso": "En Proceso", "Vendido": "Vendido", "Cancelado" : "Cancelado"}
    numeroVenta = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete= models.CASCADE,
        verbose_name= "Cliente"
        )
    monto = models.DecimalField(default= 0, decimal_places=2, max_digits= 10)
    estado = models.CharField(max_length= 100, choices=ESTADOS, default="En Proceso")
    fecha_venta = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Venta")




