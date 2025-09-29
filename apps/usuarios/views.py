from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.usuarios.models import Usuario

# Create your views here.
@login_required(login_url='index')
def lista_usuarios(request):
    return render(request=request,
                  template_name='usuarios.html',
                  context={"usuarios":Usuario.objects.all()})