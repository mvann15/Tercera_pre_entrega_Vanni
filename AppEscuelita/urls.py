from django.urls import path
from AppEscuelita.views import crear_deporte, show_html, mostrar_deportes, crear_deporte_form, buscar_categoria, \
    ver_profesores, \
    crear_profesor, profesor_form, buscar_profesor, crear_materia, materia_form, ver_materias, buscar_materia, \
    DeporteList, ProfesorList, MateriaList, DeporteDetalle, ProfesorDetalle, MateriaDetalle, DeporteCreacion, \
    ProfesorCreacion, MateriaCreacion, DeporteActualizacion, ProfesorActualizacion, MateriaActualizacion, \
    ProfesorEliminar, DeporteEliminar, MateriaEliminar

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
    path('deportes/listar', DeporteList.as_view(), name="DeportesList"),
    path('profesores/listar', ProfesorList.as_view(), name="ProfesoresList"),
    path('materias/listar', MateriaList.as_view(), name="MateriasList"),
    path('deporte/<int:pk>', DeporteDetalle.as_view(), name="DeporteDetail"),
    path('profesor/<int:pk>', ProfesorDetalle.as_view(), name="ProfesorDetail"),
    path('materia/<int:pk>', MateriaDetalle.as_view(), name="MateriaDetail"),
    path('crear_deporte', DeporteCreacion.as_view(), name="DeporteCreate"),
    path('crear_profesor', ProfesorCreacion.as_view(), name="ProfesorCreate"),
    path('crear_materia', MateriaCreacion.as_view(), name="MateriaCreate"),
    path('editar_deporte/<int:pk>', DeporteActualizacion.as_view(), name="DeporteUpdate"),
    path('editar_profesor/<int:pk>', ProfesorActualizacion.as_view(), name="ProfesorUpdate"),
    path('editar_materia/<int:pk>', MateriaActualizacion.as_view(), name="MateriaUpdate"),
    path('eliminar_deporte/<int:pk>', DeporteEliminar.as_view(), name="DeporteDelete"),
    path('eliminar_profesor/<int:pk>', ProfesorEliminar.as_view(), name="ProfesorDelete"),
    path('eliminar_materia/<int:pk>', MateriaEliminar.as_view(), name="MateriaDelete"),
]
