from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app_club/home.html')

def categoria(request):
    return render(request, 'app_club/categoria.html')

def deportista(request):
    return render(request, 'app_club/deportista.html')

def entrenador(request):
    return render(request, 'app_club/entrenador.html')

def entrenamiento(request):
    return render(request, 'app_club/entrenamiento.html')