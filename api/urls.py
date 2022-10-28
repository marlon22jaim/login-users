from django.urls import path
from .views import PersonaList


urlpatterns = [
    # as_view porque es una vista basada en clase
    path("persona/", PersonaList.as_view(), name="persona_list"),
]