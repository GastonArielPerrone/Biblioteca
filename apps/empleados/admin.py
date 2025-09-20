from django.contrib import admin

from apps.empleados.models import Empleado

# Register your models here.
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre_empleado",
                    "dni",
                    "password",
                    "telefono",
                    "cargo",
                    "fecha_contratacion",
                    "created_at",
                    "updated_at",
                    )
    search_fields = ("nombre_empleado",
                    "dni",
                    "password",
                    "telefono",
                    "cargo",
                    "fecha_contratacion",
                    "created_at",
                    "updated_at",
                    )
    list_filter = ("nombre_empleado",)