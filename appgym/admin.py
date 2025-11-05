from django.contrib import admin
from appgym.models import Socio, Instructor, Clase

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ("socio_id", "socio_nombre", "socio_apellido", "socio_docnro", "socio_fecalta")
    search_fields = ("socio_nombre", "socio_apellido", "socio_docnro")
    list_filter = ("socio_fecalta",)

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("inst_id", "inst_nombre", "inst_apellido", "inst_especialidad", "inst_turno")
    search_fields = ("inst_nombre", "inst_apellido", "inst_especialidad")
    list_filter = ("inst_turno",)

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ("clase_id", "clase_nombre", "clase_tema", "clase_horario", "clase_cupo")
    search_fields = ("clase_nombre", "clase_tema")
    list_filter = ("clase_horario",)
