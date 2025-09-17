from django.db import models

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre_autor = models.CharField(max_length=100, null=False, blank=False)
    nacionalidad = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre_autor