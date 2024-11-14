from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo','serie' ,'sinopsis', 'estreno', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopsis': forms.Textarea(attrs={'class': 'form-control'}),
            'estreno' : forms.DateInput(attrs={'type': 'date'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),

        }
