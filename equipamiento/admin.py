from django.contrib import admin
from equipamiento.models import Equipamiento

@admin.register(Equipamiento)
class EquipamientoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre_ref", "categoria", "marca", "estado", "fecha_alta")
    search_fields = ("nombre_ref", "marca", "codigo")
    list_filter = ("categoria", "estado")
