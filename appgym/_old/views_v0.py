from django.shortcuts import render, redirect
from coder.forms import *
from coder.models import Estudiante

def index(request):
    return render(request, "coder/index.html")


def test(request):
    return render(request, "coder/test.html")


def crear_estudiante(request):
    # GET - Pedir informacion a la base de datos.
    # POST - Solicitud para crear informacion/manipular informacion.
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiante_form")
    else:
        form = EstudianteForm()
    
    return render(request, "coder/estudiante_form.html", {'form': form})

def lista_estudiantes(request):
    query = request.GET.get('q', '')
    if len(query) > 0: # if query:
        estudiante = Estudiante.objects.filter(
            nombre__icontains=query).order_by("-fecha_de_creacion")
    else:
        estudiante = Estudiante.objects.all().order_by("-fecha_de_creacion")
    
    return render(request, "coder/estudiante_list.html", {"estudiantes": estudiante, "query": query})
