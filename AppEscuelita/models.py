from django.db import models


class Deporte(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre} - Categoria: {self.categoria}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    deportes_que_ensenia = models.ManyToManyField(Deporte)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    puntaje = models.IntegerField()
    deportes_relacionados = models.ManyToManyField(Deporte)

    def __str__(self):
        return f"{self.nombre} - Puntaje: {self.puntaje}"
