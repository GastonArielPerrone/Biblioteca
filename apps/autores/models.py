from django.db import models

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre_autor = models.CharField(max_length=100, null=False, blank=False)
    nacionalidad = models.CharField(max_length=50)