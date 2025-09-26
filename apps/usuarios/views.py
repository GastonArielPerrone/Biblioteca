from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.usuarios.models import Usuario

# Create your views here.
def index(request):
    if request.method == "POST":
        dni = request.POST.get('dni')
        password = request.POST.get('password')
        user = authenticate(request, dni=dni, password=password)  # si tu backend usa dni
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or request.POST.get('next') or 'lista_usuarios'
            return redirect(next_url)
        else:
            return render(request, 'index.html', {'error': 'DNI o contraseña incorrectos'})
    return render(request, 'index.html', {})

@login_required(login_url='index')
def lista_usuarios(request):
    return render(request=request,
                  template_name='usuarios.html',
                  context={"usuarios":Usuario.objects.all()})