from django.db import models

# Create your models here.

class Pessoa(models.Model):
	codigo = models.IntegerField() 
	nome = models.CharField(max_length=60) 
	rg = models.CharField(max_length=12) 
	cpf = models.CharField(max_length=15) 
	email = models.CharField(max_length=60) 
	endereco = models.CharField(max_length=80) 

	def __str__(self):
		return self.nome
