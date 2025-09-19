from rest_framework import generics
from .models import Empleado
from .serializers import EmpleadoSerializer, EmpleadoTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

class EmployeeRegistrationView(generics.CreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [AllowAny]

class EmpleadoTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmpleadoTokenObtainPairSerializer