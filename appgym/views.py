from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
import datetime
from appgym.forms import SocioForm, InstructorForm, ClaseForm
from appgym.models import Socio, Instructor, Clase
from django.contrib.auth.decorators import login_required

# ==========================
# PÁGINAS PRINCIPALES
# ==========================

def index(request):
    return render(request, "appgym/index.html")


def test(request):
    return render(request, "appgym/test.html")


def about(request):
    return render(request, "appgym/about.html")


def acerca_de_mi(request):
    return render(request, "appgym/acerca_de_mi.html")


# ==========================
# SOCIOS
# ==========================
@login_required
def crear_socio(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("socio_list")
    else:
        form = SocioForm(initial={'socio_fecalta': datetime.date.today()})
    return render(request, "appgym/socio_form.html", {'form': form})

@login_required
def lista_socios(request):
    query = request.GET.get('q', '')
    if query:
        socios = Socio.objects.filter(
            Q(socio_nombre__icontains=query) |
            Q(socio_apellido__icontains=query) |
            Q(socio_docnro__icontains=query)
        ).order_by("-socio_id")
    else:
        socios = Socio.objects.all().order_by("-socio_id")

    return render(request, "appgym/socio_list.html", {"socios": socios, "query": query})

@login_required
def visualizar_socio(request, socio_id):
    socio = get_object_or_404(Socio, socio_id=socio_id)
    return render(request, "appgym/socio_visualizar.html", {"socio": socio})

@login_required
def eliminar_socio(request, socio_id):
    socio = get_object_or_404(Socio, socio_id=socio_id)
    socio.delete()
    messages.success(request, "Socio eliminado correctamente")
    return redirect("socio_list")

@login_required
def modificar_socio(request, socio_id):
    socio = get_object_or_404(Socio, socio_id=socio_id)
    if request.method == "POST":
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect("socio_list")
    else:
        form = SocioForm(instance=socio)
    return render(request, "appgym/socio_form.html", {'form': form, 'edicion': True})


# ==========================
# INSTRUCTORES
# ==========================
@login_required
def crear_instructor(request):
    if request.method == "POST":
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("instructor_list")
    else:
        form = InstructorForm()
    return render(request, "appgym/instructor_form.html", {'form': form})

@login_required
def lista_instructores(request):
    query = request.GET.get('q', '')
    if query:
        instructores = Instructor.objects.filter(
            Q(inst_nombre__icontains=query) |
            Q(inst_apellido__icontains=query) |
            Q(inst_especialidad__icontains=query)
        ).order_by("-inst_id")
    else:
        instructores = Instructor.objects.all().order_by("-inst_id")

    return render(request, "appgym/instructor_list.html", {"instructores": instructores, "query": query})

@login_required
def visualizar_instructor(request, inst_id):
    instructor = get_object_or_404(Instructor, inst_id=inst_id)
    return render(request, "appgym/instructor_visualizar.html", {"instructor": instructor})

@login_required
def eliminar_instructor(request, inst_id):
    instructor = get_object_or_404(Instructor, inst_id=inst_id)
    instructor.delete()
    messages.success(request, "Instructor eliminado correctamente")
    return redirect("instructor_list")

@login_required
def modificar_instructor(request, inst_id):
    instructor = get_object_or_404(Instructor, inst_id=inst_id)
    if request.method == "POST":
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect("instructor_list")
    else:
        form = InstructorForm(instance=instructor)
    return render(request, "appgym/instructor_form.html", {'form': form, 'edicion': True})


# ==========================
# CLASES
# ==========================
@login_required
def crear_clase(request):
    if request.method == "POST":
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clase_list")
    else:
        form = ClaseForm()
    return render(request, "appgym/clase_form.html", {'form': form})

@login_required
def lista_clases(request):
    query = request.GET.get('q', '')
    if query:
        clases = Clase.objects.filter(
            Q(clase_nombre__icontains=query) |
            Q(clase_tema__icontains=query)
        ).order_by("-clase_id")
    else:
        clases = Clase.objects.all().order_by("-clase_id")

    return render(request, "appgym/clase_list.html", {"clases": clases, "query": query})

@login_required
def visualizar_clase(request, clase_id):
    clase = get_object_or_404(Clase, clase_id=clase_id)
    return render(request, "appgym/clase_visualizar.html", {"clase": clase})

@login_required
def eliminar_clase(request, clase_id):
    clase = get_object_or_404(Clase, clase_id=clase_id)
    clase.delete()
    messages.success(request, "Clase eliminada correctamente")
    return redirect("clase_list")

@login_required
def modificar_clase(request, clase_id):
    clase = get_object_or_404(Clase, clase_id=clase_id)
    if request.method == "POST":
        form = ClaseForm(request.POST, instance=clase)
        if form.is_valid():
            form.save()
            return redirect("clase_list")
    else:
        form = ClaseForm(instance=clase)
    return render(request, "appgym/clase_form.html", {'form': form, 'edicion': True})
