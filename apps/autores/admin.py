from django.contrib import admin
from apps.autores.models import Autor

# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre_autor", "nacionalidad")
    search_fields = ("nombre_autor", "nacionalidad")
    list_filter = ("nombre_autor", "nacionalidad",)