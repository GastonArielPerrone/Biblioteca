from django.db import models

class Autor(models.Model):
    nombre_autor = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    nacionalidad = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_autor