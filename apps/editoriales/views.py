from django.shortcuts import render, redirect
from apps.editoriales.models import Editorial
from .forms import EditorialForm

# Create your views here.
def lista_editoriales(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_editoriales')
    else:
        form = EditorialForm()
    editoriales = Editorial.objects.all()
    return render(request, 'editoriales.html', {'form': form, 'editoriales': editoriales})