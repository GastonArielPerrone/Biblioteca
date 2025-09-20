from django.db import models

class Editorial(models.Model):
    nombre_editorial = models.CharField(max_length=100, null=False, blank=False)
    pais_editorial = models.CharField(max_length=50)
    calle_editorial = models.CharField(max_length=100)
    numero_calle_editorial = models.IntegerField()
    casa_editorial = models.BooleanField(default=False)
    edificio_editorial = models.BooleanField(default=False)
    piso_editorial = models.CharField(max_length=10)
    departamento_numero_casa_editorial = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)