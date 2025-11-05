from django.urls import path
from equipamiento.views import *

urlpatterns = [
    path("", EquipamientoListView.as_view(), name="equipamiento_list"),
    path("nuevo/", EquipamientoCreateView.as_view(), name="equipamiento_create"),
    path("<str:codigo>/", EquipamientoDetailView.as_view(), name="equipamiento_detail"),
    path("<str:codigo>/editar/", EquipamientoUpdateView.as_view(), name="equipamiento_edit"),
    path("<str:codigo>/eliminar/", EquipamientoDeleteView.as_view(), name="equipamiento_delete"),
]
