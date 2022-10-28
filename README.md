# Bienvenido a mi login de usuarios 💙
### Configurando entorno
- creo el projecto en git y lo clono en mis directorios
`git clone direccionSshDeGit`


* crear entorno python
`python3 -m venv venv`


* activar entorno python
`source venv/bin/activate`


* seleccionar el interprete en VSCode
abrimos el editor y oprimimos f1 luego escribimos "python: select interpreter" y escogemos el que diga venv


* instalamos Django
`pip install django`


* instalar Django Rest Framework
`pip install djangorestframework`


* crear proyecto django
`django-admin startproject login_rest .`


* correr el servidor
`python3 manage.py runserver`


* crear app
`python3 manage.py startapp api`

- vamos a la carpeta del proyecto y en settings agregamos la nueva app, el rest framework y la zona horaria

```python
INSTALLED_APPS = [
    "rest_framework",
    "api"
]

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'
```

### Models

- vamos a la carpeta de la app llamada api y vamos al archivo models.py

```python
from django.db import models

# Create your models here.


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Nombre", max_length=100)
    apellido = models.CharField("Apellido", max_lenght=200)

    # sirve para una vista por defecto para cada instancia del modelo persona
    def __str__(self):
        return "{0}, {1}".format(self.apellido, self.name)
```

- Crear las migraciones
`python3 manage.py makemigrations`

- Hacemos la migracion
`python3 manage.py migrate`

al hacer esto se nos creara una tabla api_persona en nuestra DB

### Crear admin
- vamos a la carpeta de la aplicacion llamada api y abrimos el archivo admin.py

```python
from django.contrib import admin
from .models import Persona
# Register your models here.

admin.site.register(Persona)
```

- vamos a crear un super admin
 ` python3 manage.py createsuperuser`

