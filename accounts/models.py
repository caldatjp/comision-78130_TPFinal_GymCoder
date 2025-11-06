from django.db import models
from django.contrib.auth.models import AbstractUser


def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"

class Perfil(AbstractUser):
    avatar = models.ImageField(
        upload_to=avatar_upload_to,
        default="default/perfil/default.png",
        blank=True,
        null=True,
        verbose_name="Avatar"
    )
    pais = models.CharField(max_length=50, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(null=True)
    direccion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"


    def __str__(self):
        return f"{self.username}: {self.last_name}, {self.first_name}"