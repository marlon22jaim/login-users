from rest_framework import serializers
from .models import Persona

# creamos un serializador


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        # indicamos el modelo
        model = Persona
        # indicamos los campos que deseo, son de la DB y del modelo
        fields = (
            "id",
            "name",
            "apellido",
        )
