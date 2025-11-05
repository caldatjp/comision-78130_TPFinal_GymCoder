from django.shortcuts import render, redirect
from coder.forms import *
from coder.models import Estudiante, Socio, Instructor, Clase


def index(request):
    return render(request, "coder/index.html")


def test(request):
    return render(request, "coder/test.html")


# ==========================
# Vistas para Estudiantes
# ==========================

def crear_estudiante(request):
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
    if len(query) > 0:
        estudiante = Estudiante.objects.filter(
            nombre__icontains=query).order_by("-fecha_de_creacion")
    else:
        estudiante = Estudiante.objects.all().order_by("-fecha_de_creacion")
    
    return render(request, "coder/estudiante_list.html", {"estudiantes": estudiante, "query": query})


# ==========================
# Vistas para Socios
# ==========================

def crear_socio(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("socio_form")
    else:
        form = SocioForm()
    
    return render(request, "coder/socio_form.html", {'form': form})


def lista_socios(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        socios = Socio.objects.filter(
            socio_nombre__icontains=query).order_by("-socio_fecalta")
    else:
        socios = Socio.objects.all().order_by("-socio_fecalta")
    
    return render(request, "coder/socio_list.html", {"socios": socios, "query": query})


# ==========================
# Vistas para Instructores
# ==========================

def crear_instructor(request):
    if request.method == "POST":
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("instructor_form")
    else:
        form = InstructorForm()
    
    return render(request, "coder/instructor_form.html", {'form': form})


def lista_instructores(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        instructores = Instructor.objects.filter(
            inst_nombre__icontains=query).order_by("inst_apellido")
    else:
        instructores = Instructor.objects.all().order_by("inst_apellido")
    
    return render(request, "coder/instructor_list.html", {"instructores": instructores, "query": query})


# ==========================
# Vistas para Clases
# ==========================

def crear_clase(request):
    if request.method == "POST":
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clase_form")
    else:
        form = ClaseForm()
    
    return render(request, "coder/clase_form.html", {'form': form})


def lista_clases(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        clases = Clase.objects.filter(
            clase_nombre__icontains=query).order_by("clase_nombre")
    else:
        clases = Clase.objects.all().order_by("clase_nombre")
    
    return render(request, "coder/clase_list.html", {"clases": clases, "query": query})
