from rest_framework import generics
from .models import Prestamo
from .serializers import PrestamoReadSerializer, PrestamoWriteSerializer

class PrestamoList(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PrestamoWriteSerializer
        return PrestamoReadSerializer
