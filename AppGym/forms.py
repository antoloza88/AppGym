from django import forms

class NuevaClientaFormulario(forms.Form):
    usuario = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_de_nacimiento = forms.DateField()
    email = forms.EmailField()
    celular = forms.IntegerField()
    contraseña = forms.IntegerField()


