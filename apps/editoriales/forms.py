from django import forms
from .models import Editorial

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__'
