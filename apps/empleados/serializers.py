from rest_framework import serializers
from .models import Empleado
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id_empleado', 'dni', 'nombre_empleado', 'telefono', 'cargo', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Empleado.objects.create_user(**validated_data)
        return user

class EmpleadoTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'dni'
