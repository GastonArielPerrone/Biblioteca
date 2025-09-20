from django.contrib import admin
from apps.categorias.models import Categoria

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre_categoria",)
    search_fields = ("nombre_categoria",)
    list_filter = ("nombre_categoria",)