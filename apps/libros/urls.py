from django.urls import path
from .views import LibroList

urlpatterns = [
    path('libros/', LibroList.as_view(), name='libro-list'),
]
