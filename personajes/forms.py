from django import forms
from .models import Imagen

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['titulo', 'descripcion', 'imagen', 'Raza']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'Raza': forms.TextInput(attrs={'class': 'form-control'}),

        }