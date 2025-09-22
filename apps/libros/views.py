from django.shortcuts import render
from apps.libros.models import Libro

# Create your views here.
def lista_libros(request):
    return render(request=request, 
                template_name='libros.html', 
                context= {"libros": Libro.objects.all()},
                )