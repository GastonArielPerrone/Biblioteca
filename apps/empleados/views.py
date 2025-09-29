from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from apps.empleados.models import Empleado
from django.contrib.auth.hashers import make_password

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

Empleado = get_user_model()

def register(request):
    if request.method == "POST":
        dni = request.POST.get("dni")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        password = request.POST.get("password")
        
        # Crear empleado y guardar contraseña hasheada
        empleado = Empleado(
            dni=dni,
            nombre=nombre,
            apellido=apellido,
            password=make_password(password)
        )
        empleado.save()
        return redirect('index')  # redirige al login después de registrar

    return render(request, "register.html")

def lista_empleados(request):
    return render(request=request,
                  template_name='empleados.html',
                  context={"empleados":Empleado.objects.all()})