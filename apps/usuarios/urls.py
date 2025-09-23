from apps.usuarios.views import lista_usuarios
from django.urls import path

urlpatterns = [
    path('lista/', lista_usuarios, name='lista_usuarios')
]
