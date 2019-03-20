#classe responsável pela serialização do dados. Transforma os objetos em texto. 
from rest_framework import serializers
from cadastro import models


class PessoaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Pessoa
		fields = ('codigo','nome','rg','cpf','email','endereco',)
		depth = 1 