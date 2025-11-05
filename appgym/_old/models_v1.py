from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    nro_legajo = models.IntegerField(unique=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_nacimiento = models.DateField(null=True)
    
    def __str__(self):
        return f"Estudiante: {self.nombre} - Nro Legajo: {self.nro_legajo}"


class Examenes(models.Model):
    nota = models.FloatField()
    asignatura = models.CharField(max_length=30)
    nombre_de_estudiante = models.CharField(max_length=100)


# Nuevas clases adaptadas a la temática del gimnasio Coder
class Socio(models.Model):
    socio_id = models.AutoField(primary_key=True)
    socio_nombre = models.CharField(max_length=100)
    socio_apellido = models.CharField(max_length=100)
    socio_docnro = models.CharField(max_length=20, unique=True)
    socio_fecnacimiento = models.DateField(null=True, blank=True)
    socio_fecalta = models.DateField(null=True, blank=True)
    socio_fecbaja = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.socio_nombre} {self.socio_apellido} (DNI: {self.socio_docnro})"


class Instructor(models.Model):
    inst_id = models.AutoField(primary_key=True)
    inst_nombre = models.CharField(max_length=100)
    inst_apellido = models.CharField(max_length=100)
    inst_sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    inst_especialidad = models.CharField(max_length=100)
    inst_turno = models.CharField(max_length=20, choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde'), ('Noche', 'Noche')])

    def __str__(self):
        return f"{self.inst_nombre} {self.inst_apellido} - {self.inst_especialidad}"


class Clase(models.Model):
    clase_id = models.AutoField(primary_key=True)
    clase_nombre = models.CharField(max_length=100)
    clase_tema = models.CharField(max_length=100)  # <-- CAMBIO
    clase_horario = models.CharField(max_length=50)
    clase_cupo = models.PositiveIntegerField(default=20)

    def __str__(self):
        return f"{self.clase_nombre} ({self.clase_tema}) - Cupo: {self.clase_cupo}"

