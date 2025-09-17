from rest_framework import generics
from .models import Libro
from .serializers import LibroSerializer

class LibroList(generics.ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer