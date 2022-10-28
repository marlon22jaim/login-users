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