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


# ==========================
# FORMULARIO SOCIO
# ==========================

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = [
            "socio_nombre",
            "socio_apellido",
            "socio_docnro",
            "socio_fecnacimiento",
            "socio_fecalta",
            "socio_fecbaja",
        ]
        widgets = {
            "socio_nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "socio_apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "socio_docnro": forms.TextInput(attrs={'class': 'form-control'}),
            "socio_fecnacimiento": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "socio_fecalta": forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'value': ''}),
            "socio_fecbaja": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    # ✅ Validación DNI solo numérico y largo correcto
    def clean_socio_docnro(self):
        dni = self.cleaned_data.get("socio_docnro", "").strip()

        if not dni.isdigit():
            raise forms.ValidationError("El DNI debe contener solo números (sin letras ni símbolos).")

        if len(dni) < 7 or len(dni) > 8:
            raise forms.ValidationError("El DNI debe tener 7 u 8 dígitos.")

        return dni

    # ✅ Normalización nombre y apellido a mayúsculas y sin espacios
    def clean_socio_nombre(self):
        nombre = self.cleaned_data.get("socio_nombre", "")
        return nombre.strip().upper()

    def clean_socio_apellido(self):
        apellido = self.cleaned_data.get("socio_apellido", "")
        return apellido.strip().upper()


# ==========================
# FORMULARIO INSTRUCTOR
# ==========================

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


# ==========================
# FORMULARIO CLASE
# ==========================

class ClaseForm(forms.ModelForm):

    HORARIOS = [
        ("8:00-9:00", "8:00-9:00"),
        ("9:00-10:00", "9:00-10:00"),
        ("10:00-11:00", "10:00-11:00"),
        ("11:00-12:00", "11:00-12:00"),
        ("12:00-13:00", "12:00-13:00"),
        ("13:00-14:00", "13:00-14:00"),
        ("14:00-15:00", "14:00-15:00"),
        ("15:00-16:00", "15:00-16:00"),
        ("16:00-17:00", "16:00-17:00"),
        ("17:00-18:00", "17:00-18:00"),
        ("18:00-19:00", "18:00-19:00"),
        ("19:00-20:00", "19:00-20:00"),
        ("20:00-21:00", "20:00-21:00"),
    ]

    CUPOS = [(10, "10"), (20, "20"), (30, "30"), (40, "40")]

    clase_horario = forms.ChoiceField(choices=HORARIOS, widget=forms.Select(attrs={'class': 'form-select'}))
    clase_cupo = forms.ChoiceField(choices=CUPOS, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Clase
        fields = ["clase_nombre", "clase_tema", "clase_horario", "clase_cupo"]
        widgets = {
            "clase_nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "clase_tema": forms.TextInput(attrs={'class': 'form-control'}),
        }
