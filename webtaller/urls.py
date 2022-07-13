from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('galeria/', galeria, name='GALE'),
    path('registro/', registro,name='REGIS'),
    path('sebastian/', sebastian ,name='SEBA'),
    path('cristian/', cristian,name='CRIS'),
    path('contacto/', contacto,name='CONTAC'),
    path('autos_sebastian/', autos_sebastian,name='AUTOSEBA'),
    path('autos_cristian/', autos_cristian,name='AUTOCRIS'),
    path('autos_cristian/', autos_cristian,name='AUTOCRIS'),
    path('atencion/', atencion,name='atencion'),
    path('newatencion/', newatencion,name='newatencion'),
    path('atencionDetalle/<id>', atencionDetalle,name='atencionDetalle'),
    path('busqueda/', busqueda,name='busqueda'),
    path('modatencion/<id>', modatencion, name="modatencion"),
    path('delatencion/<id>', delatencion, name="delatencion"),
]
