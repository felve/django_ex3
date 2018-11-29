from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .serializers import interesasosSerializer, MascotaSerializer
import json

from .models import (
	Interesados,
	Mascotas,
	Estados
)

from .forms import MascotaListForm,InteresadosForm, MascotasForm, EstadosForm


def hello_world(request):
    """Ejemplo de view que sólo muestra un "Hola mundo" en el navegador."""
    return HttpResponse("Hello world!")

	
"""Administración de interesados********************************************************************************************"""

def create_interesados(request):
    """View para crear una nueva lista películas por ver."""
    if request.method == "POST":
        form = InteresadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:interesados")
        else:
            errors = form.errors
            context = {
                'form': form,
                'errors': errors
            }
            return render(request, 'movies/new_interesados.html', context)
    else:
        form = InteresadosForm()
        context = {
            'form': form
        }
        return render(request, 'movies/new_interesados.html', context)


def list_interesados(request):
    """View que enlista MovieList que hay en la base de datos."""
    lists = Interesados.objects.all().order_by('nombrecompleto')
    context =  {
        'lists': lists
    }

    return render(request, 'movies/list_interesados.html', context)

def detail_interesados(request, id):
    """View que muestra el detalle de una lista."""
    object = get_object_or_404(Interesados, pk=id)
    context = {
        'list': object
    }

    return render(request, 'movies/detail_interesados.html', context)

def update_interesados(request, id):
    """View para editar una lista."""
    object = get_object_or_404(Interesados, pk=id)
    if request.method == "POST":
        form = InteresadosForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect("movies:interesados")
        else:
            errors = form.errors
            context = {
                'form': form,
                'errors': errors
            }
            return render(request, 'movies/new_interesados.html', context)
    else:
        form = InteresadosForm(instance=object)
        context = {
            'form': form,
            'list': object
        }
        return render(request, 'movies/new_interesados.html', context)


def delete_interesados(request, id):
    """
    View para borrar una lista. Si es un método GET, le pedimos confirmación
    al usuario. Si es un método POST, significa que el usuario ha confirmado
    y podemos borrar la lista.
    """
    object = get_object_or_404(Interesados, pk=id)

    if request.method == "POST":
        object.delete()
        return redirect("movies:interesados")
    else:
        return render(request, "movies/delete_interesados.html", {'list': object})

		
		
"""Administración de Mascotas********************************************************************************************"""

def create_mascotas(request):
    """View para crear una nueva lista películas por ver."""
    if request.method == "POST":
        form = MascotasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:mascotas")
        else:
            errors = form.errors
            context = {
                'form': form,
                'errors': errors
            }
            return render(request, 'movies/new_mascotas.html', context)
    else:
        form = MascotasForm()
        context = {
            'form': form
        }
        return render(request, 'movies/new_mascotas.html', context)


def list_mascotas(request):
    """View que enlista MovieList que hay en la base de datos."""
    lists = Mascotas.objects.all().order_by('nombre')
    context =  {
        'lists': lists
    }

    return render(request, 'movies/list_mascotas.html', context)

def detail_mascotas(request, id):
    """View que muestra el detalle de una lista."""
    object = get_object_or_404(Mascotas, pk=id)
    context = {
        'list': object
    }

    return render(request, 'movies/detail_mascotas.html', context)

def update_mascotas(request, id):
    """View para editar una lista."""
    object = get_object_or_404(Mascotas, pk=id)
    if request.method == "POST":
        form = MascotasForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect("movies:mascotas")
        else:
            errors = form.errors
            context = {
                'form': form,
                'errors': errors
            }
            return render(request, 'movies/new_mascotas.html', context)
    else:
        form = MascotasForm(instance=object)
        context = {
            'form': form,
            'list': object
        }
        return render(request, 'movies/new_mascotas.html', context)


def delete_mascotas(request, id):
    """
    View para borrar una lista. Si es un método GET, le pedimos confirmación
    al usuario. Si es un método POST, significa que el usuario ha confirmado
    y podemos borrar la lista.
    """
    object = get_object_or_404(Mascotas, pk=id)

    if request.method == "POST":
        object.delete()
        return redirect("movies:mascotas")
    else:
        return render(request, "movies/delete_mascotas.html", {'list': object})

		
""" Detalle desde los estados"""
def create_estados(request):
    """View para crear una nueva lista películas por ver."""
    if request.method == "POST":
        form = Estados(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:estados")
        else:
            errors = form.errors
            context = {
                'form': form,
                'errors': errors
            }
            return render(request, 'movies/new_estados.html', context)
    else:
        form = EstadosForm()
        context = {
            'form': form
        }
        return render(request, 'movies/new_estados.html', context)


def list_estados(request):
    """View que enlista MovieList que hay en la base de datos."""
    lists = Estados.objects.all().order_by('name')
    context =  {
        'lists': lists
    }

    return render(request, 'movies/list_estados.html', context)

def detail_estados(request, id):
    """View que muestra el detalle de una lista."""
    object = get_object_or_404(Mascotas, pk=id)
    context = {
        'list': object
    }

    return render(request, 'movies/detail_estados.html', context)

def update_estados(request, id):
    """View para editar una lista."""
    object = get_object_or_404(Estados, pk=id)
    if request.method == "POST":
        form = EstadosForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect("movies:estados")
        else:
            errors = form.errors
            context = {
                'form': form,
                'errors': errors
            }
            return render(request, 'movies/new_estados.html', context)
    else:
        form = EstadosForm(instance=object)
        context = {
            'form': form,
            'list': object
        }
        return render(request, 'movies/new_estados.html', context)


def delete_estados(request, id):
    """
    View para borrar una lista. Si es un método GET, le pedimos confirmación
    al usuario. Si es un método POST, significa que el usuario ha confirmado
    y podemos borrar la lista.
    """
    object = get_object_or_404(Mascotas, pk=id)

    if request.method == "POST":
        object.delete()
        return redirect("movies:estados")
    else:
        return render(request, "movies/delete_estados.html", {'list': object})


class InteresadosList(generics.ListCreateAPIView):
	queryset = Interesados.objects.all()
	serializer_class = interesasosSerializer	
	
	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj
			
class MascotasList(generics.ListCreateAPIView):
	queryset = Mascotas.objects.all()
	serializer_class = MascotaSerializer
	
	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj			

def index1(request):
    template='movies/index1.html'
    results=interesados.objects.all()
    context={
        'results':results,
    }
    return render(request,template,context)