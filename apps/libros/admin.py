from django.contrib import admin

from apps.libros.models import Libro

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo",
                    "autor",
                    "editorial",
                    "categoria",
                    "fecha_publicacion",
                    "cantidad",
                    "creado",
                    "actualizado",)
    search_fields = ("titulo",
                    "autor__nombre",
                    "editorial__nombre",
                    "categoria__nombre",
                    "fecha_publicacion",
                    "cantidad",
                    "creado",
                    "actualizado",)
    list_filter = ("autor",
                    "editorial",
                    "categoria",)