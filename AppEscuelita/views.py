from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from AppEscuelita.models import Deporte, Profesor, Materia
from AppEscuelita.forms import DeporteForm, BuscarDeporteForm, ProfesorForm, BuscarProfesorForm, MateriaForm, \
    BuscarMateriaForm


class DeporteList(ListView):
    model = Deporte
    template_name = "AppEscuelita/deportes_1.html"


class DeporteDetalle(DetailView):
    model = Deporte
    template_name = "AppEscuelita/deportes_detalle.html"


class DeporteCreacion(CreateView):
    model = Deporte
    success_url = "/app/deportes/listar"
    template_name = "AppEscuelita/crear_deporte.html"
    fields = ["nombre", "categoria"]


class DeporteActualizacion(UpdateView):
    model = Deporte
    success_url = "/app/deportes/listar"
    template_name = "AppEscuelita/crear_deporte.html"
    fields = ["nombre", "categoria"]


class DeporteEliminar(DeleteView):
    model = Deporte
    success_url = "/app/deportes/listar"
    template_name = "AppEscuelita/eliminar_deporte.html"
    fields = ["nombre", "categoria"]


def mostrar_deportes(request):
    deportes = Deporte.objects.all()
    contexto = {
        "deportes": deportes,
        "form": BuscarDeporteForm(),
    }

    return render(request, 'AppEscuelita/deportes.html', contexto)


def crear_deporte(request):
    deporte = Deporte(nombre="", categoria=5)
    deporte.save()

    return redirect("/app/deportes/")


def crear_deporte_form(request):
    if request.method == "POST":
        deporte_formulario = DeporteForm(request.POST)

        if deporte_formulario.is_valid():
            informacion = deporte_formulario.cleaned_data
            deporte_crear = Deporte(nombre=informacion["nombre"], categoria=informacion["categoria"])
            deporte_crear.save()
            return redirect("/app/deportes/")

    deporte_formulario = DeporteForm()
    contexto = {
        "form": deporte_formulario
    }
    return render(request, "AppEscuelita/crear_deporte.html", contexto)


def buscar_categoria(request):
    try:
        nombre = request.GET["nombre"]
        deportes = Deporte.objects.filter(nombre__icontains=nombre)
        contexto = {
            "deportes": deportes,
            "form": BuscarDeporteForm(),
        }

        return render(request, "AppEscuelita/deportes.html", contexto)

    except MultiValueDictKeyError:
        return redirect("/app/deportes/")


class ProfesorList(ListView):
    model = Profesor
    template_name = "AppEscuelita/profesor_1.html"


class ProfesorDetalle(DetailView):
    model = Profesor
    template_name = "AppEscuelita/profesores_detalle.html"


class ProfesorCreacion(CreateView):
    model = Profesor
    success_url = "/app/profesores/listar"
    template_name = "AppEscuelita/crear_profesor.html"
    fields = ["nombre", "apellido", "email"]


class ProfesorActualizacion(UpdateView):
    model = Profesor
    success_url = "/app/profesores/listar"
    template_name = "AppEscuelita/crear_profesor.html"
    fields = ["nombre", "apellido", "email"]


class ProfesorEliminar(DeleteView):
    model = Profesor
    success_url = "/app/profesores/listar"
    template_name = "AppEscuelita/eliminar_profesor.html"
    fields = ["nombre", "apellido", "email"]


def crear_profesor(request):
    profesor = Profesor(nombre="Ramiro", apellido="Vasquez", email="ramirov@escuelita.ar")
    profesor.save()

    return redirect("/app/profesores/")


def ver_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {
        "profesores": profesores,
        "form": BuscarProfesorForm(),
    }

    return render(request, 'AppEscuelita/profesores.html', contexto)


def profesor_form(request):
    if request.method == "POST":
        profesor_formulario = ProfesorForm(request.POST)

        if profesor_formulario.is_valid():
            informacion = profesor_formulario.cleaned_data
            profesor_crear = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"],
                                      email=informacion["email"])
            profesor_crear.save()
            return redirect("/app/profesores/")

    profesor_formulario = ProfesorForm()
    contexto = {
        "form": profesor_formulario
    }
    return render(request, "AppEscuelita/crear_profesor.html", contexto)


def buscar_profesor(request):
    try:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre__icontains=nombre)
        contexto = {
            "profesores": profesores,
            "form": BuscarProfesorForm(),
        }

        return render(request, "AppEscuelita/profesores.html", contexto)

    except MultiValueDictKeyError:
        return redirect("/app/profesores/")


def crear_materia(request):
    materia = Materia(nombre="Futbol", puntaje="95")
    materia.save()

    return redirect("/app/materias/")


class MateriaList(ListView):
    model = Materia
    template_name = "AppEscuelita/materia_1.html"


class MateriaDetalle(DetailView):
    model = Materia
    template_name = "AppEscuelita/materias_detalle.html"


class MateriaCreacion(CreateView):
    model = Materia
    success_url = "/app/materias/listar"
    template_name = "AppEscuelita/crear_materia.html"
    fields = ["nombre", "puntaje"]


class MateriaActualizacion(UpdateView):
    model = Materia
    success_url = "/app/materias/listar"
    template_name = "AppEscuelita/crear_materia.html"
    fields = ["nombre", "puntaje"]


class MateriaEliminar(DeleteView):
    model = Materia
    success_url = "/app/materias/listar"
    template_name = "AppEscuelita/eliminar_materia.html"
    fields = ["nombre", "puntaje"]


def ver_materias(request):
    materias = Materia.objects.all()
    contexto = {
        "materias": materias,
        "form": BuscarMateriaForm(),
    }

    return render(request, 'AppEscuelita/materias.html', contexto)


def materia_form(request):
    if request.method == "POST":
        materia_formulario = MateriaForm(request.POST)

        if materia_formulario.is_valid():
            informacion = materia_formulario.cleaned_data
            materia_crear = Materia(nombre=informacion["nombre"], puntaje=informacion["puntaje"])
            materia_crear.save()
            return redirect("/app/materias/")

    materia_formulario = MateriaForm()
    contexto = {
        "form": materia_formulario
    }
    return render(request, "AppEscuelita/crear_materia.html", contexto)


def buscar_materia(request):
    try:
        nombre = request.GET["nombre"]
        materias = Materia.objects.filter(nombre__icontains=nombre)
        contexto = {
            "materias": materias,
            "form": BuscarMateriaForm(),
        }

        return render(request, "AppEscuelita/materias.html", contexto)

    except MultiValueDictKeyError:
        return redirect("/app/materias/")


def show_html(request):
    deporte = Deporte.objects.first()
    profesor = Profesor.objects.first()
    materia = Materia.objects.first()
    contexto = {"deporte": deporte, "profesor": profesor, "materia": materia}
    return render(request, 'index.html', contexto)
