from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class NuevaClientaFormulario(forms.Form):
    usuario = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_de_nacimiento = forms.DateField()
    email = forms.EmailField()
    celular = forms.IntegerField()
    contraseña = forms.IntegerField()


class EditarUsuarioFormulario(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email' , 'password1', 'password2']
        help_text = {k:"" for k in fields}

