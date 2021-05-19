# from django.contrib import admin
# Register your models here.

from django.contrib import admin
#from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from .models import Area1

# class ListarAreas(OSMGeoAdmin):
# admin.ModelAdmin
class ListarAreas(LeafletGeoAdmin):
    list_display = ('id', 'sigla', 'nome', 'telefone', 'geom')
    list_display_links = ('sigla', 'nome')
    search_fields = ('sigla', 'nome',)
    list_per_page = 20

# Register your models here.
admin.site.register(Area1, ListarAreas)
