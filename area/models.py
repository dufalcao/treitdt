# from django.db import models
# Create your models here.

from django.contrib.gis.db import models

# local = PointField(srid=4326, blank=True, null=True)
# default='POINT(0.0 0.0)

class Area1(models.Model): 
    sigla = models.CharField(max_length=5, unique=True) 
    nome = models.CharField(max_length=50, unique=True) 
    desc_referenciada = models.TextField() 
    desc_especialidades = models.TextField() 
    telefone = models.CharField(max_length=15) 
    foto = models.ImageField(upload_to='static/img', blank=True, null=True)
    geom = models.PointField('Localização', srid=4326, geography=True, blank=True, null=True)
    def __str__ (self): 
        return self.nome 
    
    @property
    def popup_content(self):
        popup = f'<div class="row"><div class="col-sm-6"><img src="{self.foto}" class="rounded foto"></div>'
        popup += f'<div class="col-sm-6"> Sigla: <span>{self.sigla}</span>'
        popup += f'<p>Nome: <span>{self.nome}</span></p>'
        popup += f'<p>Telefone: <span>{self.telefone}</span></p>'
        popup += f'Descrição Especialidades: <span>{self.desc_especialidades}</span></div></div>'
        return popup

#     <div class="row"><div class="col">
    
    # @property
    # def popup_content(self):
    #     popup = f"Sigla: <span>{self.sigla}</span>"
    #     popup += f"<p>Nome: <span>{self.nome}</span></p>"
    #     popup += f"<p>Telefone: <span>{self.telefone}</span></p>"
    #     popup += f"Descrição Especialidades: <span>{self.desc_especialidades}</span>"
    #     popup += f'<img src="{self.foto}" class=" rounded-circle foto">'
    #     return popup

    # @property
    # def popupContent(self):
    #   return '<img src="{}" /><p><{}</p>'.format(
    #       self.foto.url,
    #       self.nome,
    #       self.desc_especialidades)

