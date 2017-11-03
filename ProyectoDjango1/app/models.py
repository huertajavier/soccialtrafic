"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User

class Usuario_m(models.Model):
	Nombre = models.OneToOneField(User)
	Telefono = models.IntegerField()
	Correo = models.CharField(max_length=50)
	Direccion = models.CharField(max_length=100)
	Avatar = models.FileField(upload_to='avatar/%Y/%m/%d', null=True)

	def __unicode__(self):
		return self.Correo


class Denuncia_m(models.Model):
	user=models.ForeignKey(User)
	titulo=models.CharField(max_length=50)
	descripcion=models.TextField()
	latitud=models.FloatField()
	longitud=models.FloatField()
	img = models.FileField(upload_to='img/%Y/%m/%d', null=True)
	video = models.FileField(upload_to='videos/%Y/%m/%d', null=True)

	def __unicode__(self):
		return self.titulo


