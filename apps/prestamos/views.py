from django.shortcuts import render, redirect
from apps.prestamos.models import Prestamo
from apps.prestamos.forms import PrestamoForm
from apps.libros.models import Libro

def lista_prestamos(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save()
            libro = prestamo.titulo_libro
            if libro.cantidad > 0:
                libro.cantidad -= 1
                libro.save()
            else:
                form.add_error('titulo_libro', 'Libro no está disponible. ☹️')
                return render(request, 'prestamos.html', {'form': form, 'prestamos': Prestamo.objects.all()})
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm()
    
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos.html', {'prestamos': prestamos, 'form': form})