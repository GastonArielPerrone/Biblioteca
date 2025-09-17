from rest_framework import serializers
from .models import Libro
from apps.autores.serializers import AutorSerializer
from apps.editoriales.serializers import EditorialSerializer
from apps.categorias.serializers import CategoriaSerializer

class LibroSerializer(serializers.ModelSerializer):
    id_autor = AutorSerializer()
    id_editorial = EditorialSerializer()
    id_categoria = CategoriaSerializer()

    class Meta:
        model = Libro
        fields = '__all__'
