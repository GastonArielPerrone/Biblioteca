from django.shortcuts import render, redirect
from apps.autores.models import Autor
from .forms import AutorForm

# Create your views here.
def lista_autores(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'form': form, 'autores': autores})