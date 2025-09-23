from django.db import models
from django.contrib.auth.hashers import make_password, check_password #Herramienta para hashear y chequear password.
class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=100, null=False, blank=False)
    dni = models.CharField(max_length=15, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128)
    telefono = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)
    fecha_contratacion = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def guardar(self, *args, **kwargs): #Guarda password hasheándolo si no está hasheado.
        # Solo hashear si la contraseña no está ya hasheada
        if not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def checkeo_password(self, raw_password): #Verifica si la contraseña coincide con el hash.
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return self.nombre_empleado