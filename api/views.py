from rest_framework import generics
from .models import Persona
from .serializers import PersonaSerializer


# Create your views here.
# ListCreateApiView para poder crear y no solo ver
class PersonaList(generics.ListCreateAPIView):
    # consulta, trae todas las personas
    queryset = Persona.objects.all()
    # indicamos que modelo serializador voy a usar
    serializer_class = PersonaSerializer
