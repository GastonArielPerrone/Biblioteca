from django import forms
from apps.usuarios.models import Usuario

class RegistrationForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=150, required=False, label="Nombre")
    dni = forms.CharField(max_length=20, label="DNI")
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono")
    calle = forms.CharField(max_length=255, required=False, label="Dirección")
    numero_calle = forms.IntegerField(required=False, label="Número de calle")
    casa = forms.BooleanField(required=False, label="Casa")
    edificio = forms.BooleanField(required=False, label="Edificio")
    piso = forms.CharField(max_length=10, required=False, label="Piso")
    departamento_numero_casa = forms.CharField(max_length=10, required=False, label="Departamento/Número de casa")

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if dni:
            dni = str(dni).strip()
            if Usuario.objects.filter(dni=dni).exists():
                raise forms.ValidationError("Ya existe un usuario con ese DNI")
        return dni