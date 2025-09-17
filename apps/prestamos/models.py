from django.db import models
from apps.libros.models import Libro
from apps.usuarios.models import Usuario

class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=False, blank=False)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False)
    fecha_prestamo = models.DateField(auto_now_add=True)
    hora_prestamo = models.TimeField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    hora_devolucion = models.TimeField(null=True, blank=True)
    estado = models.CharField(max_length=10, default='pendiente')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        return f"Préstamo de {self.id_libro.titulo_libro} a {self.id_usuario.nombre_usuario}"