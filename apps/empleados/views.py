from django.shortcuts import render
from apps.empleados.models import Empleado

# Create your views here.
def lista_empleados(request):
    return render(request=request,
                  template_name='empleados.html',
                  context={"empleados":Empleado.objects.all()})