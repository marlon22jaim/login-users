from django.db import models

# Create your models here.


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Nombre", max_length=100)
    apellido = models.CharField("Apellido", max_length=200)

    # sirve para una vista por defecto para cada instancia del modelo persona
    def __str__(self):
        # vista desde el admin
        return "{0}, {1}".format(self.apellido, self.name)
