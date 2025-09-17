from rest_framework import serializers
from .models import Prestamo
from apps.libros.serializers import LibroSerializer
from apps.usuarios.serializers import UsuarioSerializer
from apps.libros.models import Libro
from apps.usuarios.models import Usuario

# Serializer for reading prestamos (with nested details)
class PrestamoReadSerializer(serializers.ModelSerializer):
    id_libro = LibroSerializer()
    id_usuario = UsuarioSerializer()

    class Meta:
        model = Prestamo
        fields = '__all__'

# Serializer for writing prestamos (with simple IDs)
class PrestamoWriteSerializer(serializers.ModelSerializer):
    id_libro = serializers.PrimaryKeyRelatedField(queryset=Libro.objects.all())
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())

    class Meta:
        model = Prestamo
        fields = ('id_libro', 'id_usuario')