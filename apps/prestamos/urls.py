from django.urls import path
from apps.prestamos.views import lista_prestamos

urlpatterns = [
    path('lista/', lista_prestamos, name='lista_prestamos')
]
