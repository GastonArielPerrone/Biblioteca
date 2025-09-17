from django.urls import path
from .views import PrestamoList

urlpatterns = [
    path('prestamos/', PrestamoList.as_view(), name='prestamo-list'),
]
