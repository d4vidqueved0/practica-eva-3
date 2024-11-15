from django.urls import path
from . import views

app_name = 'peliculas'

urlpatterns = [
    path('', views.lista_peliculas, name='lista_peliculas'),
    path('pelicula/<int:pk>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('subir/', views.subir_pelicula, name='subir_pelicula'),
    path('pelicula/<int:pk>/editar/', views.editar_pelicula, name='editar_pelicula'),
    path('pelicula/<int:pk>/eliminar/', views.eliminar_pelicula, name='eliminar_pelicula'),


]