from django.contrib import admin

from apps.libros.models import Libro

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo_libro",
                    "autor",
                    "editorial",
                    "categoria",
                    "fecha_publicacion",
                    "cantidad",
                    "creado",
                    "actualizado",)
    search_fields = ("titulo_libro",
                    "nombre_autor",
                    "nombre_editorial",
                    "nombre_categoria",
                    "fecha_publicacion",
                    "cantidad",
                    "creado",
                    "actualizado",)
    list_filter = ("autor",
                    "editorial",
                    "categoria",)