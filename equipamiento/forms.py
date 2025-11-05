from django import forms
from equipamiento.models import Equipamiento

class EquipamientoForm(forms.ModelForm):
    class Meta:
        model = Equipamiento
        fields = [
            'nombre_ref',
            'categoria',
            'marca',
            'peso',
            'nro_serie',
            'estado',
            'fecha_baja',
        ]
        widgets = {
            'nombre_ref': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'nro_serie': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'fecha_baja': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Preformatear fecha_baja si existe (para datetime-local input)
        if self.instance and self.instance.fecha_baja:
            self.initial['fecha_baja'] = self.instance.fecha_baja.strftime('%Y-%m-%dT%H:%M')
