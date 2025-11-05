from django import forms
from coder.models import Estudiante


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
