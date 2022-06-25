from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    disciplina = models.CharField(max_length=40)

    def __str__(self):
        return f'Categoria: {self.nombre} -- Año: {self.año} -- Disciplina: {self.disciplina}'


class Deportista(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    disciplina = models.CharField(max_length=40)
    disponibilidad = models.BooleanField()

    def __str__(self):
        disponibilidad = 'Si' if self.disponibilidad else 'No'
        return f'Nombre del Deportista: {self.nombre} {self.apellido} -- Disciplina: {self.disciplina} -- Disponibilidad: {disponibilidad}'


class Entrenador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    disciplina = models.CharField(max_length=40)

    def __str__(self):
        return f'Nombre del Entrenador: {self.nombre} {self.apellido} -- Disciplina: {self.disciplina}'


class Entrenamiento(models.Model):
    fecha = models.DateField()
    disciplina = models.CharField(max_length=40)

    def __str__(self):
        return f'Fecha de entrenamiento: {self.fecha} -- Disciplina: {self.disciplina}'


class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Subcarpeta avatares de media :)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f'url: {self.image.url}'