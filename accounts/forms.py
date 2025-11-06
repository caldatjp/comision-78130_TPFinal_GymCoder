from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Perfil


class PerfilCreationForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ("username", "email", "avatar")


class PerfilChangeForm(UserChangeForm):
    class Meta:
        model = Perfil
        fields = ("avatar", "pais", "direccion", "first_name", "last_name", "password", "username")

        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control", "placeholder": "País"}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Dirección"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apellido"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de usuario"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "readonly": "readonly"}),
        }
        
        