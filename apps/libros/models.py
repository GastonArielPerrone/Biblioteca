from django.db import models
from apps.autores.models import Autor
from apps.editoriales.models import Editorial
from apps.categorias.models import Categoria

class Libro(models.Model):
    titulo_libro = models.CharField(max_length=200, null=False, blank=False, primary_key=True)
    nombre_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=False, blank=False)
    nombre_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, null=False, blank=False)
    nombre_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False)
    fecha_publicacion = models.DateTimeField()
    cantidad = models.IntegerField(null=False, blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)