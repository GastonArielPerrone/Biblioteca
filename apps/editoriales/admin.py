from django.contrib import admin

from apps.editoriales.models import Editorial

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    # usa los nombres exactos de los campos de tu modelo
    list_display = (
        'id',
        'nombre_editorial',
        'pais_editorial',
        'calle_editorial',
        'numero_calle_editorial',
        'tipo_ubicacion',  # columna calculada (ver método abajo)
        'piso_editorial',
        'departamento_numero_casa_editorial',
        'created_at',
        'updated_at',
    )

    search_fields = ('nombre_editorial', 'pais_editorial', 'calle_editorial')
    list_filter = ('pais_editorial', 'casa_editorial', 'edificio_editorial', 'created_at')

    # columna calculada que combina casa/edificio y muestra algo legible
    def tipo_ubicacion(self, obj):
        partes = []
        if getattr(obj, 'casa_editorial', False):
            partes.append('Casa')
        if getattr(obj, 'edificio_editorial', False):
            partes.append('Edificio')
        if not partes:
            partes.append('—')
        return " / ".join(partes)
    tipo_ubicacion.short_description = 'Tipo de ubicación'
    tipo_ubicacion.admin_order_field = 'casa_editorial'  # opcional: ordena por este campo
