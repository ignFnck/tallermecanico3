from django.contrib import admin
from .models import *
# Register your models here.

class ImagenAtencionAdmin(admin.TabularInline):
    model = ImagenAtencion

class AtencionAdmin(admin.ModelAdmin):
    list_display = ['id','tipoate','descripcion','publicar','categoria','usuario']
    search_fields = ['id','tipoate']
    list_filter = ['tipoate','categoria']
    list_per_page = 4
    inlines = [
        ImagenAtencionAdmin
    ]

admin.site.register(Categoria)

admin.site.register(tipoAte)

admin.site.register(Contacto)

admin.site.register(Atencion, AtencionAdmin)