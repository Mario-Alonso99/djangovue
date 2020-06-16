from rest_framework import viewsets
from .models import Element
from .serializer import ElementSerializer

class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer