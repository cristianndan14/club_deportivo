from django.forms import model_to_dict
from django.shortcuts import render
from app_club.forms import *
from app_club.models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required # --> sirve para proteger funciones, y solo permitir a usuarios


# Create your views here.
def index(request):
    return render(request, 'app_club/home.html')


def categoria(request):
    categoria = Categoria.objects.all()

    context_dict = {
        'categoria' : categoria,
    }

    return render(
        request=request, 
        context=context_dict,
        template_name='app_club/categoria.html'
    )


def deportista(request):
    deportista = Deportista.objects.all()

    context_dict = {
        'deportista' : deportista,
    }

    return render(
        request=request, 
        context=context_dict,
        template_name='app_club/deportista.html'
    )


def entrenador(request):
    entrenador = Entrenador.objects.all()

    context_dict = {
        'entrenador' : entrenador,
        }

    return render(
        request=request,
        context=context_dict,
        template_name='app_club/entrenador.html'
    )


def entrenamiento(request):
    entrenamiento = Entrenamiento.objects.all()

    context_dict = {
        'entrenamiento' : entrenamiento,
    }

    return render(
        request=request, 
        context=context_dict,
        template_name='app_club/entrenamiento.html'
    )


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
    context_dict = dict()
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


# ---------------- CRUD --------------


def delete_entrenador(request, pk: int):
    entrenador = Entrenador.objects.get(pk=pk)
    
    if request.method == 'POST':
        entrenador.delete()

        entrenador = Entrenador.objects.all()
        context_dict = {
            'entrenador': entrenador,
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_club/entrenador.html"
        )

    context_dict = {
        'entrenador': entrenador,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_club/entrenador_confirm_delete.html'
    )


def update_entrenador(request, pk: int):
    entrenador = Entrenador.objects.get(pk=pk)

    if request.method == 'POST':
        entrenador_form = EntrenadorForm(request.POST)
        if entrenador_form.is_valid():
            data = entrenador_form.cleaned_data
            entrenador.nombre = data['nombre']
            entrenador.apellido = data['apellido']
            entrenador.disciplina = data['disciplina']
            entrenador.save()

            entrenador = Entrenador.objects.all()
            context_dict = {
                'entrenador': entrenador
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_club/entrenador.html"
            )

    entrenador_form = EntrenadorForm(model_to_dict(entrenador))
    context_dict = {
        'entrenador': entrenador,
        'entrenador_form': entrenador_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_club/entrenador_form.html'
    )


# ---------- CRUD CON "ListView" y sus derivados ------
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin # --> Otra forma de realizar el login_required


class CategoriaListView(ListView):
    model = Categoria
    template_name = "app_club/categoria_list.html"


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = "app_club/categoria_detail.html"


class CategoriaCreateView(LoginRequiredMixin, CreateView): # --> SIEMPRE colocar el login antes que la vista.
    model = Categoria
    success_url = reverse_lazy('app_club:categoria-list')
    fields = ['nombre', 'año', 'disciplina']


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    success_url = reverse_lazy('app_club:categoria-list')
    fields = ['nombre', 'año', 'disciplina']


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy('app_club:categoria-list')



# ------------ Login / Logout / Register -------------
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from app_club.forms import UserRegisterForm # --> importando el form personalizado


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                template_name = "app_club/home.html"
        else:
            template_name = "app_club/login.html"
        return render(
            request=request,
            context={'form': form},
            template_name=template_name,
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="app_club/login.html"
    )


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST) # ---> Usando el form de django
        form = UserRegisterForm(request.POST) # ---> Personalizando el form, usando de base el de django
        if form.is_valid():
            form.save()
            return render(
                request=request,
                context={"mensaje": "Usuario registrado satisfactoriamente."},
                template_name="app_club/login.html"
            )
    # form = UserCreationForm()
    form = UserRegisterForm()
    return render(
        request=request,
        context={"form": form},
        template_name="app_club/register.html"
    )


def logout_request(request):
    logout(request)
    return redirect("app_club:Home")