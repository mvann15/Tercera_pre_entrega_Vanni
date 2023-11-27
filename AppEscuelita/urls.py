from django.urls import path
from AppEscuelita.views import crear_deporte, show_html, mostrar_deportes, crear_deporte_form, buscar_categoria, \
    ver_profesores, \
    crear_profesor, profesor_form, buscar_profesor, crear_materia, materia_form, ver_materias, buscar_materia

urlpatterns = [
    path('crear/', crear_deporte),
    path('nuevo/', crear_profesor),
    path('nueva/', crear_materia),
    path('deporte/', crear_deporte_form),
    path('profesor/', profesor_form),
    path('materia/', materia_form),
    path('deportes/', mostrar_deportes),
    path('profesores/', ver_profesores),
    path('materias/', ver_materias),
    path('buscar/', buscar_categoria),
    path('ver/', buscar_profesor),
    path('mostrar/', buscar_materia),
    path('show/', show_html),
]
