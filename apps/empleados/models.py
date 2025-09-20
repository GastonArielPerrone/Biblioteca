from django.db import models

class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    dni = models.CharField(max_length=15, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128)
    telefono = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)
    fecha_contratacion = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre_empleado