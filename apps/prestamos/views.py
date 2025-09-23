from django.shortcuts import render
from apps.prestamos.models import Prestamo

# Create your views here.
def lista_prestamos(request):
    return render(request=request,
                  template_name='prestamos.html',
                  context={"prestamos":Prestamo.objects.all()})