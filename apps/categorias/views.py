from django.shortcuts import render, redirect
from apps.categorias.models import Categoria
from .forms import CategoriaForm

# Create your views here.
def lista_categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'form': form, 'categorias': categorias})