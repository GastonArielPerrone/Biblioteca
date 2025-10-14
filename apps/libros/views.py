# apps/libros/views.py
from django.shortcuts import render, redirect
from django.contrib import admin
from .models import Libro
from .forms import LibroForm

admin.register(Libro)
def lista_libros(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    libros = Libro.objects.all()
    return render(request, 'libros.html', {'form': form, 'libros': libros})
