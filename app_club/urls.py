from django.contrib import admin
from django.urls import path, include
from app_club.views import *

urlpatterns = [
    path('', index, name='Home'),
    path('categoria', categoria),
    path('deportista', deportista),
    path('entrenador', entrenador),
    path('entrenamiento', entrenamiento),
]
