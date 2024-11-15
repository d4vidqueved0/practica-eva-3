from django.db import models
from django.contrib.auth.models import User

class Imagen(models.Model):
    # Definir las opciones para el campo 'raza' como una tupla de tuplas
    RAZAS = (
        ('Humano', 'Humano'),
        ('Namekiano', 'Namekiano'),
        ('Saiyajin', 'Saiyajin'),
    )

    titulo = models.CharField(max_length=200)
    raza = models.CharField(max_length=10, choices=RAZAS)  # Añadir choices aquí
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

