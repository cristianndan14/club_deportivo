from django.contrib import admin
from django.urls import path, include
from app_club.views import *

urlpatterns = [
    path('', index, name='Home'),
    path('categoria', categoria, name='Categoria'),
    path('deportista', deportista, name='Deportista'),
    path('entrenador', entrenador, name='Entrenador'),
    path('entrenamiento', entrenamiento, name='Entrenamiento'),
    path('categoria_form', categoria_form, name='Categoria_form'),
    path('deportista_form', deportista_form, name='Deportista_form'),
    path('entrenador_form', entrenador_form, name='Entrenador_form'),
    path('entrenamiento_form', entrenamiento_form, name='Entrenamiento_form'),
    path('busqueda', busqueda, name='Busqueda'),
]
