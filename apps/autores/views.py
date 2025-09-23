from django.shortcuts import render
from apps.autores.models import Autor

# Create your views here.
def lista_autores(request):
    return render(request=request,
                  template_name='autores.html',
                  context={"autores":Autor.objects.all()})