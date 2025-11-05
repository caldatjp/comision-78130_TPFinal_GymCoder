from django import forms
from coder.models import Estudiante, Socio, Instructor, Clase


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["nombre", "apellido", "email", "nro_legajo", "fecha_de_nacimiento"]
        widgets = {
            "fecha_de_nacimiento": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "nro_legajo": forms.NumberInput(attrs={'class': 'form-control'})
        }


# -------------------------------
# Nuevos formularios para Gimnasio Coder
# -------------------------------

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = [
            "socio_nombre",
            "socio_apellido",
            "socio_docnro",
            "socio_fecnacimiento",
            "socio_fecalta",
            "socio_fecbaja"
        ]
        widgets = {
            "socio_nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "socio_apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "socio_docnro": forms.TextInput(attrs={'class': 'form-control'}),
            "socio_fecnacimiento": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "socio_fecalta": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "socio_fecbaja": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = [
            "inst_nombre",
            "inst_apellido",
            "inst_sexo",
            "inst_especialidad",
            "inst_turno"
        ]
        widgets = {
            "inst_nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "inst_apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "inst_sexo": forms.Select(attrs={'class': 'form-select'}),
            "inst_especialidad": forms.TextInput(attrs={'class': 'form-control'}),
            "inst_turno": forms.Select(attrs={'class': 'form-select'}),
        }


class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = [
            "clase_nombre",
            "clase_especialidad",
            "clase_horario",
            "clase_cupo"
        ]
        widgets = {
            "clase_nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "clase_especialidad": forms.TextInput(attrs={'class': 'form-control'}),
            "clase_horario": forms.TextInput(attrs={'class': 'form-control'}),
            "clase_cupo": forms.NumberInput(attrs={'class': 'form-control'}),
        }
