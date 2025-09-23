from django.shortcuts import render
from apps.categorias.models import Categoria

# Create your views here.
def lista_categorias(request):
    return render(request=request,
                  template_name='categorias.html',
                  context={"categorias":Categoria.objects.all()})