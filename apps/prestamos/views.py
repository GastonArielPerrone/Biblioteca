from rest_framework import generics, status
from rest_framework.response import Response
from .models import Prestamo
from apps.libros.models import Libro
from .serializers import PrestamoReadSerializer, PrestamoWriteSerializer

class PrestamoList(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PrestamoWriteSerializer
        return PrestamoReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        id_libro = serializer.validated_data['id_libro'].id_libro
        libro = Libro.objects.get(pk=id_libro)
        
        if libro.cantidad > 0:
            libro.cantidad -= 1
            libro.save()
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'error': 'No hay stock disponible para este libro.'}, status=status.HTTP_400_BAD_REQUEST)
