from django.db import models
import uuid


def generar_code():
    return uuid.uuid4().hex


class Equipamiento(models.Model):
    ESTADOS = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('mantenimiento', 'En mantenimiento'),
        ('baja', 'De baja'),
    ]

    CATEGORIAS = [
        ('cardio', 'Cardio'),
        ('fuerza', 'Fuerza'),
        ('accesorio', 'Accesorio'),
        ('estiramiento', 'Estiramiento'),
        ('funcional', 'Funcional'),
        # agrega más si querés...
    ]

    codigo = models.CharField(max_length=32, unique=True, default=generar_code)
    nombre_ref = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    marca = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=6, decimal_places=2)  # kg
    nro_serie = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activo')
    fecha_alta = models.DateTimeField(auto_now_add=True)
    fecha_baja = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_ref} ({self.codigo}) - Estado: {self.get_estado_display()} - Categoria: {self.get_categoria_display()}"
