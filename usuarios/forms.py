from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class RegistroForm(forms.ModelForm):#Clase para el formulario de registro
    username = forms.CharField(widget=forms.TextInput (attrs={'class':'form-control'}), label="Nombre de usuario")
    email =  forms.CharField(widget=forms.EmailInput (attrs={'class':'form-control'}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Contraseña')
    password_confirmacion = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Confirmar Contraseña')
    rol = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=Perfil.ROLES, label='Rol')

    class Meta:#Clase Meta para definir el modelo y los campos del formulario
        model = User
        fields = ['username', 'email', 'password', 'password_confirmacion']#Campos del formulario

    #Método para validar la confirmación de la contraseña, se llama clean_<nombre_campo>
    def clean_password_confirmacion(self):#Método para validar la confirmación de la contraseña
        password = self.cleaned_data.get('password')#Obtenemos la contraseña
        password_confirmacion = self.cleaned_data.get('password_confirmacion')
        if password and password_confirmacion and password != password_confirmacion:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password_confirmacion
