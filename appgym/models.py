from django.db import models


# ==========================
# SOCIO
# ==========================

class Socio(models.Model):
    socio_id = models.AutoField(primary_key=True)
    socio_nombre = models.CharField(max_length=100)
    socio_apellido = models.CharField(max_length=100)
    socio_docnro = models.CharField(max_length=20, unique=True)
    socio_fecnacimiento = models.DateField(null=True, blank=True)
    socio_fecalta = models.DateField(null=True, blank=True)
    socio_fecbaja = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.socio_nombre:
            self.socio_nombre = self.socio_nombre.strip().upper()
        if self.socio_apellido:
            self.socio_apellido = self.socio_apellido.strip().upper()
        if self.socio_docnro:
            self.socio_docnro = self.socio_docnro.strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.socio_nombre} {self.socio_apellido} (DNI: {self.socio_docnro})"


# ==========================
# INSTRUCTOR
# ==========================

class Instructor(models.Model):
    inst_id = models.AutoField(primary_key=True)
    inst_nombre = models.CharField(max_length=100)
    inst_apellido = models.CharField(max_length=100)
    inst_sexo = models.CharField(max_length=10, choices=[
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ])
    inst_especialidad = models.CharField(max_length=100)
    inst_turno = models.CharField(max_length=20, choices=[
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche')
    ])

    def save(self, *args, **kwargs):
        if self.inst_nombre:
            self.inst_nombre = self.inst_nombre.strip().upper()
        if self.inst_apellido:
            self.inst_apellido = self.inst_apellido.strip().upper()
        if self.inst_especialidad:
            self.inst_especialidad = self.inst_especialidad.strip().upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.inst_nombre} {self.inst_apellido} - {self.inst_especialidad}"


# ==========================
# CLASE
# ==========================

class Clase(models.Model):
    clase_id = models.AutoField(primary_key=True)
    clase_nombre = models.CharField(max_length=100)
    clase_tema = models.CharField(max_length=100)
    clase_horario = models.CharField(max_length=50)
    clase_cupo = models.PositiveIntegerField(default=20)

    def save(self, *args, **kwargs):
        if self.clase_nombre:
            self.clase_nombre = self.clase_nombre.strip().upper()
        if self.clase_tema:
            self.clase_tema = self.clase_tema.strip().upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.clase_nombre} ({self.clase_tema}) - Cupo: {self.clase_cupo}"
