from django.conf.urls import url

from . import views
from django.contrib import admin
from movies.views import InteresadosList,MascotasList

app_name= 'movies'

urlpatterns = [
    url(
        regex=r'^hello/$',
        view=views.hello_world,
        name='hello_world'
    ),

    url(
        regex=r'^interesados/$',
        view=views.list_interesados,
        name='list'
    ),

    url(
        regex=r'^crear-lista/$',
        view=views.create_interesados,
        name='new_interesados'
    ),

    url(
        regex=r'^listas/$',
        view=views.list_interesados,
        name='interesados'
    ),

    url(
        regex=r'^listas/(?P<id>\d+)/$',
        view=views.detail_interesados,
        name='detail_interesados'
    ),

    url(
        regex=r'^editar-lista/(?P<id>\d+)/$',
        view=views.update_interesados,
        name='edit_interesados'
    ),

    url(
        regex=r'^borrar-lista/(?P<id>\d+)/$',
        view=views.delete_interesados,
        name='delete_interesados'
    ),

    url(
        regex=r'^mascotas/$',
        view=views.list_mascotas,
        name='listmascotas'
    ),

    url(
        regex=r'^crear-mascota/$',
        view=views.create_mascotas,
        name='new_mascotas'
    ),

    url(
        regex=r'^listas_mascotas/$',
        view=views.list_mascotas,
        name='mascotas'
    ),

    url(
        regex=r'^listas_mascotas/(?P<id>\d+)/$',
        view=views.detail_mascotas,
        name='detail_mascotas'
    ),

    url(
        regex=r'^editar-mascotas/(?P<id>\d+)/$',
        view=views.update_mascotas,
        name='edit_mascotas'
    ),

    url(
        regex=r'^borrar-mascota/(?P<id>\d+)/$',
        view=views.delete_mascotas,
        name='delete_mascotas'
    ),

    url(
        regex=r'^estados/$',
        view=views.list_estados,
        name='listestados'
    ),

    url(
        regex=r'^crear-estados/$',
        view=views.create_estados,
        name='new_estados'
    ),

    url(
        regex=r'^listas_estados/$',
        view=views.list_estados,
        name='estados'
    ),

    url(
        regex=r'^listas_estados/(?P<id>\d+)/$',
        view=views.detail_estados,
        name='detail_estados'
    ),

    url(
        regex=r'^editar-estados/(?P<id>\d+)/$',
        view=views.update_estados,
        name='edit_estados'
    ),

    url(
        regex=r'^borrar-estados/(?P<id>\d+)/$',
        view=views.delete_estados,
        name='delete_estados'
    ),
	url(r'^interesadoslist/', InteresadosList.as_view(), name='interesadoslist'),
	url(r'^mascotaslist/', MascotasList.as_view(), name='mascotaslist')
]
