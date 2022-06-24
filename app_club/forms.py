from django import forms
from django.forms import ModelForm
from app_club.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoriaForm(forms.Form):
    nombre = forms.CharField(max_length=40, min_length=3, label='Nombre')
    año = forms.IntegerField(label='Año')
    disciplina = forms.CharField(max_length=40, min_length=3, label='Disciplina')


class DeportistaForm(forms.Form):
    nombre = forms.CharField(max_length=40, min_length=3, label='Nombre')
    apellido = forms.CharField(max_length=40, min_length=3, label='Apellido')
    disciplina = forms.CharField(max_length=40, min_length=3, label='Disciplina')
    disponibilidad = forms.BooleanField(label='Disponible', required=False)


class EntrenadorForm(forms.Form):
    nombre = forms.CharField(max_length=40, min_length=3, label='Nombre')
    apellido = forms.CharField(max_length=40, min_length=3, label='Apellido')
    disciplina = forms.CharField(max_length=40, min_length=3, label='Disciplina')


class EntrenamientoForm(forms.Form):
    fecha = forms.DateField(
        label='Fecha de entrenamiento',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    disciplina = forms.CharField(max_length=40, min_length=3, label='Disciplina')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario', min_length=3)
    first_name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}