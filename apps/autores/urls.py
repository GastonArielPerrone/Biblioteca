from apps.autores.views import lista_autores
from django.urls import path

urlpatterns = [
    path('lista/', lista_autores, name='lista_autores')
]