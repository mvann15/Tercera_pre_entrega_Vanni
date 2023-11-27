from django import forms


class DeporteForm(forms.Form):
    nombre = forms.CharField()
    categoria = forms.IntegerField()


class BuscarDeporteForm(forms.Form):
    nombre = forms.CharField()


class ProfesorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()


class BuscarProfesorForm(forms.Form):
    nombre = forms.CharField()


class MateriaForm(forms.Form):
    nombre = forms.CharField()
    puntaje = forms.IntegerField()


class BuscarMateriaForm(forms.Form):
    nombre = forms.CharField()
