from apps.empleados.views import lista_empleados
from django.urls import path

urlpatterns = [
    path('lista/', lista_empleados, name='lista_empleados')
]
