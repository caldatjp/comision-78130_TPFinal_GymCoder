from django.urls import path
from .views import (
    # Páginas principales
    index,
    test,
    about,
    acerca_de_mi,

    # Socios
    crear_socio,
    lista_socios,
    visualizar_socio,
    eliminar_socio,
    modificar_socio,

    # Instructores
    crear_instructor,
    lista_instructores,
    visualizar_instructor,
    eliminar_instructor,
    modificar_instructor,

    # Clases
    crear_clase,
    lista_clases,
    visualizar_clase,
    eliminar_clase,
    modificar_clase,
)

urlpatterns = [
    # ==========================
    # Páginas principales
    # ==========================
    path("", index, name="index"),
    path("test/", test, name="test"),
    path("about/", about, name="about"),
    path("acerca-de-mi/", acerca_de_mi, name="acerca_de_mi"),

    # ==========================
    # Socios
    # ==========================
    path("socios/nuevo/", crear_socio, name="socio_form"),
    path("socios/", lista_socios, name="socio_list"),
    path("socios/<int:socio_id>/ver/", visualizar_socio, name="socio_visualizar"),
    path("socios/<int:socio_id>/editar/", modificar_socio, name="modificar_socio"),
    path("socios/<int:socio_id>/eliminar/", eliminar_socio, name="eliminar_socio"),

    # ==========================
    # Instructores
    # ==========================
    path("instructores/nuevo/", crear_instructor, name="instructor_form"),
    path("instructores/", lista_instructores, name="instructor_list"),
    path("instructores/<int:inst_id>/ver/", visualizar_instructor, name="instructor_visualizar"),
    path("instructores/<int:inst_id>/editar/", modificar_instructor, name="modificar_instructor"),
    path("instructores/<int:inst_id>/eliminar/", eliminar_instructor, name="eliminar_instructor"),

    # ==========================
    # Clases
    # ==========================
    path("clases/nuevo/", crear_clase, name="clase_form"),
    path("clases/", lista_clases, name="clase_list"),
    path("clases/<int:clase_id>/ver/", visualizar_clase, name="clase_visualizar"),
    path("clases/<int:clase_id>/editar/", modificar_clase, name="modificar_clase"),
    path("clases/<int:clase_id>/eliminar/", eliminar_clase, name="eliminar_clase"),
]
