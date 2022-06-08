from django import forms
from django.forms import ModelForm
from app_club.models import *


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