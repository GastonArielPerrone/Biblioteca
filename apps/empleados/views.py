from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from apps.empleados.models import Empleado, EmpleadoManager
from typing import cast

# Create your views here.
def index(request):
    if request.method == "POST":
        dni = request.POST.get('dni')
        password = request.POST.get('password')
        user = authenticate(request, dni=dni, password=password)  # si tu backend usa dni
        if user is not None:
            login(request, user)
            # Priorizar next si viene en GET/POST, si no, redirigir a la lista de usuarios
            next_url = request.GET.get('next') or request.POST.get('next')
            # Si el usuario es un empleado (o staff), enviarlo a la vista de usuarios
            if not next_url:
                try:
                    # Aquí asumimos que los empleados tienen is_staff=True o son instancia de Empleado
                    if getattr(user, 'is_staff', False) or user.__class__.__name__ == 'Empleado':
                        next_url = 'lista_usuarios'
                except Exception:
                    next_url = 'index'
            return redirect(next_url)
        else:
            return render(request, 'index.html', {'error': 'DNI o contraseña incorrectos'})
    return render(request, 'index.html', {})

# Usamos la clase Empleado importada directamente para que el analizador de tipos
# conozca el manager específico y su método create_user
# Empleado = get_user_model()

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                cast(EmpleadoManager, Empleado.objects).create_user(
                    dni=data['dni'],
                    password=data['password'],
                    nombre=data.get('nombre', ''),
                    apellido=data.get('apellido', ''),
                    email=data.get('email', ''),
                    telefono=data.get('telefono', ''),
                )
            except Exception as e:
                # Error al crear (por ejemplo, race condition de duplicado)
                return render(request, "register.html", {"form": form, "error": f"Error al crear el usuario: {e}"})
            return redirect('index')
        else:
            return render(request, "register.html", {"form": form})

    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})

def lista_empleados(request):
    return render(request=request,
                  template_name='empleados.html',
                  context={"empleados":Empleado.objects.all()})