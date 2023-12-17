from django.db import models
from .models import *
from django.contrib.auth.models import User


class Mecanico(models.Model):
    
    rut = models.CharField(max_length=70, default='1-0')
    nombre = models.CharField(max_length=70)
    edad = models.IntegerField(default=0)   
    apellido = models.CharField(max_length=80)    
    email = models.EmailField(default='example@example.com')
    especialista = models.CharField(max_length=100, default='Sin especialidad')      
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="Mecanico", null=True)
    descripcion = models.CharField(max_length=80, default='0')
    

    def __str__(self):
        return self.nombre
    

class Trabajo(models.Model):
    CATEGORIAS_CHOICES = [
        ('Mantencion', 'Mantencion'),
        ('Reparacion', 'Reparacion'),
        ('Diagnostico', 'Diagnostico'),
    ]

    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    imagenes = models.ImageField(upload_to="Trabajos", null=True)
    autorizado = models.BooleanField(default=False)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES, default="Mantencion")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo

class Administrador(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=80)        
    fecha = models.DateField()
    motivo_rechazo = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    


tipos_contacto = [
    [0, "Sugerencia"],
    [1, "Reclamo"]
]


    
class Contacto(models.Model):
       nombre = models.CharField(max_length=50)
       email = models.CharField(max_length=100)
       telefono = models.IntegerField()
       tipo_contacto = models.IntegerField(choices=tipos_contacto)
       mensaje = models.TextField()

       def __str__(self):
           return self.nombre + " "+self.email 
       


    
class Imagen(models.Model):
    imagen = models.ImageField(upload_to="Trabajos")
    # Puedes agregar campos adicionales según tus necesidades, como título, descripción, etc.

    def __str__(self):
        return self.imagen.name
    

class Curriculum(models.Model):
    nombre = models.CharField(max_length=70)
    segundo_nombre= models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    segundo_apellido = models.CharField(max_length=70)
    rut = models.CharField(max_length=70, default='1-0')
    fecha_nacimiento = models.DateField(null=True)
    numero_telefono = models.IntegerField(null=True)    
    email = models.EmailField(max_length=60)
    foto = models.ImageField(upload_to="Curriculums", null=True)
    experiencia = models.TextField(max_length=2000)
    especialidad = models.CharField(max_length=30, null=True)
    
    

