from django.urls import path
from .views import index, test, crear_estudiante, lista_estudiantes

urlpatterns = [
    path("", index, name="index"),
    path("test/", test , name="test"),
    path("estudiantes/nuevo", crear_estudiante, name="estudiante_form"),
    path("estudiantes/", lista_estudiantes, name="estudiante_list"),
]