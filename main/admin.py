from django.contrib import admin
from .models import Cliente,Venta, Contacto

# Register your models here.

class ContactoInline(admin.TabularInline):
    model = Cliente.contactos.through
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "contactos":
            kwargs["queryset"] = Contacto.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)



class Contacto_Admin(admin.ModelAdmin):
    list_display = ("id", "nombre" , "apellido" ,"email", "telefono")
    inlines = [ContactoInline]

class Cliente_Admin(admin.ModelAdmin):
    list_display = ("id", "nombreCliente", "is_empresa")

admin.site.register(Cliente, Cliente_Admin)
admin.site.register(Venta)
admin.site.register(Contacto, Contacto_Admin)

    