from django import forms
from apps.prestamos.models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = [
            'titulo_libro',
            'nombre_usuario',
            'nombre',
        ]
