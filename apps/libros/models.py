from django.db import models
from apps.autores.models import Autor
from apps.editoriales.models import Editorial
from apps.categorias.models import Categoria

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=False, blank=False)
    id_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, null=False, blank=False)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False)
    titulo_libro = models.CharField(max_length=200, null=False, blank=False)
    fecha_publicacion = models.DateTimeField()
    cantidad = models.IntegerField(null=False, blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo_libro