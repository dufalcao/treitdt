from rest_framework import serializers
from .models import Area1

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area1
        fields = ['sigla', 'nome', 'desc_referenciada', 'desc_especialidades', 'telefone']