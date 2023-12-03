from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from AppEscuelita.models import Deporte, Profesor, Materia


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


class MateriaList(ListView):
    model = Materia
    template_name = "AppEscuelita/materia_1.html"


class MateriaDetalle(DetailView):
    model = Materia
    template_name = "AppEscuelita/materias_detalles.html"


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
