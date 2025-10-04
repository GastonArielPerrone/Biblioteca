from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from apps.usuarios.models import Usuario
from apps.usuarios.forms import RegistrationForm

# Create your views here.
@login_required(login_url='index')
def lista_usuarios(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                Usuario.objects.create(
                    dni=data['dni'],
                    nombre=data['nombre_usuario'],
                    apellido=data['apellido'],
                    email=data.get('email', ''),
                    telefono=data.get('telefono', ''),
                    calle=data.get('calle', ''),
                    numero_calle=data.get('numero_calle', 0),
                    casa=data.get('casa', False),
                    edificio=data.get('edificio', False),
                    piso=data.get('piso', ''),
                    departamento_numero_casa=data.get('departamento_numero_casa', ''),
                    fecha_nacimiento=data.get('fecha_nacimiento', None)
                )
                return redirect('lista_usuarios')  # Evita resubmisión del formulario
            except Exception as e:
                error_msg = f"Error al crear el usuario: {e}"
                usuarios = Usuario.objects.all()
                return render(request, "usuarios.html", {"form": form, "usuarios": usuarios, "error": error_msg})
    else:
        form = RegistrationForm()

    usuarios = Usuario.objects.all()
    return render(request, "usuarios.html", {"usuarios": usuarios, "form": form})