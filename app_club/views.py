from django.shortcuts import render
from app_club.forms import *
from app_club.models import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'app_club/home.html')


def categoria(request):
    categoria = Categoria.objects.all()

    context_dict = {
        'categoria' : categoria,
    }

    return render(request=request, 
    context=context_dict,
    template_name='app_club/categoria.html')


def deportista(request):
    deportista = Deportista.objects.all()

    context_dict = {
        'deportista' : deportista,
    }

    return render(request=request, 
    context=context_dict,
    template_name='app_club/deportista.html')


def entrenador(request):
    entrenador = Entrenador.objects.all()

    context_dict = {
        'entrenador' : entrenador,
        }

    return render(request=request,
     context=context_dict,
     template_name='app_club/entrenador.html')


def entrenamiento(request):
    entrenamiento = Entrenamiento.objects.all()

    context_dict = {
        'entrenamiento' : entrenamiento,
    }

    return render(request=request, 
    context=context_dict,
    template_name='app_club/entrenamiento.html')


def categoria_form(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        if categoria_form.is_valid():
            data = categoria_form.cleaned_data
            categoria = Categoria(nombre=data['nombre'], 
            año=data['año'], 
            disciplina=data['disciplina']
            )
            categoria.save()

            categoria = Categoria.objects.all()
            context_dict = {
                'categoria' : categoria,
            }

            return render(
                request=request, 
                context=context_dict, 
                template_name="app_club/categoria.html"
                )
    
    categoria_form = CategoriaForm(request.POST)
    context_dict = {
        'categoria_form' : categoria_form,
    }

    return render(
        request=request, 
        context=context_dict, 
        template_name="app_club/categoria_form.html"
        )


def deportista_form(request):
    if request.method == 'POST':
        deportista_form = DeportistaForm(request.POST)
        if deportista_form.is_valid():
            data = deportista_form.cleaned_data
            deportista = Deportista(
                nombre=data['nombre'], 
                apellido=data['apellido'], 
                disciplina=data['disciplina'], 
                disponibilidad=data['disponibilidad']
                )
            deportista.save()

            deportista = Deportista.objects.all()
            context_dict = {
                'deportista' : deportista,
            }

            return render(
                request=request, 
                context=context_dict, 
                template_name="app_club/deportista.html"
                )
    
    deportista_form = DeportistaForm(request.POST)
    context_dict = {
        'deportista_form' : deportista_form,
    }

    return render(
        request=request, 
        context=context_dict, 
        template_name="app_club/deportista_form.html"
        )


def entrenador_form(request):
    if request.method == 'POST':
        entrenador_form = EntrenadorForm(request.POST)
        if entrenador_form.is_valid():
            data = entrenador_form.cleaned_data
            entrenador = Entrenador(
                nombre=data['nombre'], 
                apellido=data['apellido'], 
                disciplina=data['disciplina']
                )
            entrenador.save()

            entrenador = Entrenador.objects.all()
            context_dict = {
                'entrenador' : entrenador,
            }

            return render(
                request=request, 
                context=context_dict, 
                template_name="app_club/entrenador.html"
                )
    
    entrenador_form = EntrenadorForm(request.POST)
    context_dict = {
        'entrenador_form' : entrenador_form,
    }

    return render(
        request=request, 
        context=context_dict, 
        template_name="app_club/entrenador_form.html"
        )


def entrenamiento_form(request):
    if request.method == 'POST':
        entrenamiento_form = EntrenamientoForm(request.POST)
        if entrenamiento_form.is_valid():
            data = entrenamiento_form.cleaned_data
            entrenamiento = Entrenamiento(
                fecha=data['fecha'],  
                disciplina=data['disciplina']
                )
            entrenamiento.save()

            entrenamiento = Entrenamiento.objects.all()
            context_dict = {
                'entrenamiento' : entrenamiento,
            }

            return render(
                request=request, 
                context=context_dict, 
                template_name="app_club/entrenamiento.html"
                )
    
    entrenamiento_form = EntrenamientoForm(request.POST)
    context_dict = {
        'entrenamiento_form' : entrenamiento_form,
    }

    return render(
        request=request, 
        context=context_dict, 
        template_name="app_club/entrenamiento_form.html"
        )


def busqueda(request):
    if request.GET['texto_busqueda']:
        busqueda_param = request.GET['texto_busqueda']
        categoria = Categoria.objects.filter(nombre__contains=busqueda_param)
        context_dict = {
            'categoria' : categoria,
        }
    elif request.GET['año_busqueda']:
        busqueda_param = request.GET['año_busqueda']
        categoria = Categoria.objects.filter(año__contains=busqueda_param)
        context_dict = {
            'categoria' : categoria,
        }
    elif request.GET['disciplina_busqueda']:
        busqueda_param = request.GET['disciplina_busqueda']
        categoria = Categoria.objects.filter(disciplina__contains=busqueda_param)
        context_dict = {
            'categoria' : categoria,
        }
    elif request.GET['all_busqueda']:
        busqueda_param = request.GET['all_busqueda']
        query = Q(nombre__contains=busqueda_param)
        query.add(Q(año__contains=busqueda_param), Q.OR)
        categoria = Categoria.objects.filter(query)
        context_dict = {
            'categoria' : categoria,
        }
    
    return render(
        request=request,
        context=context_dict,
        template_name="app_club/home.html"
    )