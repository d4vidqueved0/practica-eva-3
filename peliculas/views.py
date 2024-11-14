from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pelicula
from .forms import PeliculaForm
from django.contrib.auth.decorators import login_required

def lista_peliculas(request):
    peliculas = Pelicula.objects.all().order_by('-fecha_subida')
    return render(request, 'peliculas/lista_peliculas.html', {'peliculas': peliculas})

def detalle_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'peliculas/detalle_pelicula.html', {'pelicula': pelicula,'request':request})

@login_required
def subir_pelicula(request):
    if request.user.perfil.rol in ['editor', 'administrador']:
        if request.method == 'POST':
            form = PeliculaForm(request.POST, request.FILES)
            if form.is_valid():
                pelicula = form.save(commit=False)
                pelicula.autor = request.user
                pelicula.save()
                return redirect('peliculas:detalle_pelicula', pk=pelicula.pk)
        else:
            form = PeliculaForm()
        return render(request, 'peliculas/subir_pelicula.html', {'form': form})
    else:
        return redirect('peliculas:lista_peliculas')

@login_required
def editar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.user == pelicula.autor or request.user.perfil.rol == 'administrador':
        if request.method == 'POST':
            form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
            if form.is_valid():
                form.save()
                messages.success(request, 'Pelicula actualizada exitosamente.')
                return redirect('peliculas:detalle_pelicula', pk=pelicula.pk)
        else:
            form = PeliculaForm(instance=pelicula)
        return render(request, 'peliculas/editar_pelicula.html', {'form': form, 'pelicula': pelicula})
    else:
        messages.error(request, 'No tienes permiso para editar esta pelicula.')
        return redirect('peliculas:detalle_pelicula', pk=pk)
    
@login_required
def eliminar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.user == pelicula.autor or request.user.perfil.rol == 'administrador':
        if request.method == 'POST':
            pelicula.delete()
            messages.success(request, 'Pelicula eliminada exitosamente.')
            return redirect('peliculas:lista_peliculas')
        else:
            return render(request, 'peliculas/eliminar_pelicula.html', {'pelicula': pelicula})
    else:
        messages.error(request, 'No tienes permiso para eliminar esta pelicula.')
        return redirect('peliculas:detalle_pelicula', pk=pk)