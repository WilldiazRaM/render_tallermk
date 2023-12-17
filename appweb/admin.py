from django.contrib import admin
from .models import *

#register you models here:
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email']
    list_editable = ['email']
    search_fields = ['nombre', 'email']

class MecanicoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cargo', 'fecha_nacimiento']
    list_editable = ['cargo']
    search_fields = ['nombre', 'apellido', 'rut']
    list_filter = ['cargo']

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cargo', 'fecha']
    search_fields = ['nombre', 'apellido']
    list_filter = ['cargo']


admin.site.register(Mecanico)
admin.site.register(Administrador)
admin.site.register(Contacto) 
admin.site.register(Trabajo)
admin.site.register(Curriculum)