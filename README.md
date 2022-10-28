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
    apellido = models.CharField("Apellido", max_length=200)

    # sirve para una vista por defecto para cada instancia del modelo persona
    def __str__(self):
        # vista desde el admin
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
 `python3 manage.py createsuperuser`

- vamos al admin y agregamos personas
http://127.0.0.1:8000/admin/

### Creando serializer y vista
- vamos a la carpeta de la aplicacion y creamos un archivo llamado serializers.py

** UN SERIALIZADOR ES UN CONVERTIDOR DE  DATA A UN TIPO JSON
SERIALIZAREMOS NUESTRO MODELO PARA CREAR UNA API PARA PODER FORMATEARLO**

```python
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

```

Ahora necesitamos una vista que nos muestre el listado de mis personas registradas en la DB

- vamos a la carpeta de la aplicacion e ingresamos al archivo views.py

```python
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
```
### Creando rutas
- En la carpeta de la app vamos a crear un archivo llamado urls.py

```python
from django.urls import path
from .views import PersonaList


urlpatterns = [
    # as_view porque es una vista basada en clase
    path("persona/", PersonaList.as_view(), name="persona_list"),
]
```

- ahora en la carpeta del projectos vamos al archivo de rutas urls.py y enlazamos los archivos de rutas de mi app y mi proyecto

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # include recibe tuplas
    path("api/1.0/", include(("api.urls","api"))),
]
```
En este momento podemos ir a la ruta http://127.0.0.1:8000/api/1.0/persona/ y agregar personas nuevas (Solo para probar)

 #### Configurando autenticación
- Vamos a la carpeta del proyecto y luego al archivo settings.py alli aremos lo siguiente

```python
INSTALLED_APPS = [
    "rest_framework.authtoken",

]

REST_FRAMEWORK = {
    # este sera el metodo de autenticacion usado para las clases asociadas a una ruta
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    # verificar que se haya iniciado sesion antes de poder acceder y mostrar los datos del API
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

```

Ahora las rutas estan protegidas

- vamos a la carpeta del projecto y en el archivo urls.py hacemos lo siguiente

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # include recibe tuplas
    path("api/1.0/", include(("api.urls","api"))),
    # hacemos una peticion a la vista view y nos responderá con un token creado para el usuario correspondiente
    path("api_generate_token/", views.obtain_auth_token),
]
```

###### Debido a que necesitamos agregar los campos de authtoken debemos hacer otra vez migraciones

`python3 manage.py migrate`

Esto nos crea una tabla nueva llamada authtoken_token en la DB
 y podemos probrar en postman

