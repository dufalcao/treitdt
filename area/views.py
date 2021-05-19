from django.shortcuts import render
from rest_framework import viewsets
from djgeojson.views import GeoJSONLayerView

from .models import Area1

class AreaGeoJson(GeoJSONLayerView):
    model = Area1
    properties = ('popup_content',)

    


# def area_js(request):
#     areas = Area1.objects.all()
#     context = {
#         'object_list': areas,
#     }
#     return render(request, 'area/area_js.html', context)