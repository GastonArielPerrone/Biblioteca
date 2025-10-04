from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.usuarios.models import Usuario
from apps.usuarios.forms import RegistrationForm

# Create your views here.
@login_required(login_url='index')
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    form = RegistrationForm()
    return render(request, "usuarios.html", {"usuarios": usuarios, "form": form})
    
def creat_usuaurio(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                Usuario.objects.create(
                    dni=data['dni'],
                    nombre=data['nombre_usuario'],
                    telefono=data.get('telefono', ''),
                    calle=data.get('calle', ''),
                    numero_calle=data.get('numero_calle', 0),
                    casa=data.get('casa', False),
                    edificio=data.get('edificio', False),
                    piso=data.get('piso', ''),
                    departamento_numero_casa=data.get('departamento_numero_casa', '')
                )
            except Exception as e:
                error_msg = f"Error al crear el usuario: {e}"
                return render(request, "usuarios.html", {"form": form, "error": error_msg})
            return render(request, "usuarios.html", {"success": "Usuario registrado exitosamente"})
        else:
            return render(request, "usuarios.html", {"form": form})
    else:
        form = RegistrationForm()
    return render(request, "usuarios.html", {"form": form})            