from django.db import models
#from django import forms
from tinymce import models as tinymce_models
# from mongoengine import *
# Create your models here.
ELECCIONES_CATEGORIA = (
	('MED', "MEDICINA"),
	('FIS', 'FISIOTERAPIA'),
	('ODO', 'ODONTOLOGIA'),
	('EST', 'ESTUDIANTIL'),
)

class Articulo(models.Model):
	"""docstring foUserme"""
	titulo = models.CharField(max_length=250)#StringField(max_length=200)
	autor = models.CharField(max_length=200)
	contenido = tinymce_models.HTMLField()
	imagen = models.ImageField(upload_to = 'static/img/')
	etiqueta = models.CharField(max_length=3, choices=ELECCIONES_CATEGORIA, default='MED')
	fecha = models.DateTimeField('fecha de publicacion')
	#def __init__(self, arg):
	#	superUsere, self).__init__()
	#	self.arg = arg
