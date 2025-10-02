# apps/libros/views.py
from django.shortcuts import render
from django.contrib import admin
from .models import Libro

admin.register(Libro)
def lista_libros(request):
    return render(request, 'libros.html', {'libros': Libro.objects.all()})
