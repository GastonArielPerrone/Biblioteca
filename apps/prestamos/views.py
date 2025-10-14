from django.shortcuts import render, redirect, get_object_or_404
from apps.prestamos.models import Prestamo
from apps.prestamos.forms import PrestamoForm
from apps.libros.models import Libro
from django.utils import timezone

def lista_prestamos(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            libro = prestamo.titulo_libro
            if libro.cantidad > 0:
                libro.cantidad -= 1
                libro.save()
                prestamo.save()
                return redirect('lista_prestamos')
            else:
                form.add_error('titulo_libro', 'Libro no está disponible. ☹️')
    else:
        form = PrestamoForm()
    
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos.html', {'prestamos': prestamos, 'form': form})

def devolver_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)
    if request.method == 'POST':
        if not prestamo.fecha_devolucion:
            prestamo.fecha_devolucion = timezone.now().date()
            prestamo.hora_devolucion = timezone.now().time()
            prestamo.estado = 'devuelto'
            prestamo.save()

            libro = prestamo.titulo_libro
            libro.cantidad += 1
            libro.save()
    return redirect('lista_prestamos')