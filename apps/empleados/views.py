from rest_framework import generics
from .models import Empleado
from .serializers import EmpleadoSerializer
from rest_framework.permissions import AllowAny

class EmployeeRegistrationView(generics.CreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [AllowAny]