from django.urls import path

from . import views as v

app_name = 'area'

urlpatterns = [
    path('geojson/', v.AreaGeoJson.as_view(), name='area_geojson'), 
]

# path('areas.js/', v.areas_js, name='areas_js'),