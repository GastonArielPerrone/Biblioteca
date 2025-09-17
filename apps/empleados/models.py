from django.db import models

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=100, null=False, blank=False)
    dni = models.CharField(max_length=15, unique=True, null=False, blank=False)
    telefono = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)
    fecha_contratacion = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre_empleado