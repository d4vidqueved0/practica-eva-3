from django.db import models
from django.contrib.auth.models import User

class Pelicula(models.Model):
    Series = (
        ('Dragon Ball', 'Dragon Ball'),
        ('Dragon Ball Z', 'Dragon Ball Z'),
        ('Dragon Ball Super', 'Dragon Ball Super'),

    )
    titulo = models.CharField(max_length=200)
    serie =models.CharField(max_length=30,choices=Series,default='Dragon Ball Z')
    sinopsis = models.TextField(max_length=1000)
    estreno = models.DateField()
    imagen = models.ImageField(upload_to='peliculas/')

    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo