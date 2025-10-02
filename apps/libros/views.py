from django.shortcuts import render
from apps.libros.models import Libro
from django.db.models import Min

# Create your views here.
def lista_libros(request):
    pks = Libro.objects.values('titulo_libro').annotate(id=Min('id')).values('id')
    libros = Libro.objects.filter(pk__in=pks)
    return render(request=request, 
                template_name='libros.html', 
                context= {"libros": libros},
                )