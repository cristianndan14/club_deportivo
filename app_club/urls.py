from django.contrib import admin
from django.urls import path
from app_club.views import *


app_name='app_club'
urlpatterns = [
    path('', index, name='Home'),
    # path('categoria', categoria, name='Categoria'),
    path('deportista', deportista, name='Deportista'),
    path('entrenador', entrenador, name='Entrenador'),
    path('entrenamiento', entrenamiento, name='Entrenamiento'),
    path('categoria_form', categoria_form, name='Categoria_form'),
    path('deportista_form', deportista_form, name='Deportista_form'),
    path('entrenador_form', entrenador_form, name='Entrenador_form'),
    path('entrenamiento_form', entrenamiento_form, name='Entrenamiento_form'),
    path('entrenador/<int:pk>/delete', delete_entrenador, name='DeleteEntrenador'),
    path('entrenador/<int:pk>/update', update_entrenador, name='UpdateEntrenador'),
    path('busqueda', busqueda, name='Busqueda'),
    # A partir de acá empiezo a usar las view de django para simplificar código ('ListView')
    path('categorias', CategoriaListView.as_view(), name='categoria-list'),
    path('categoria/add/', CategoriaCreateView.as_view(), name='categoria-add'),
    path('categoria/<int:pk>/detail', CategoriaDetailView.as_view(), name='categoria-detail'),
    path('categoria/<int:pk>/update', CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categoria/<int:pk>/delete', CategoriaDeleteView.as_view(), name='categoria-delete'),
    # ------------ Login / Logout / Register ------------- #
    path('login', login_request, name='user-login'),
    path('logout', logout_request, name='user-logout'),
    path('register', register, name='user-register'),
]
