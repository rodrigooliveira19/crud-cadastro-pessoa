from django.shortcuts import render
from cadastro import models 
from api_rest import serializers
from rest_framework import generics
from rest_framework.views import APIView 
from rest_framework.response import Response



# Create your views here.

class PessoaListServiceView(generics.ListCreateAPIView):
	queryset = models.Pessoa.objects.all()
	serializer_class = serializers.PessoaSerializer



class CadastrarPessoaServiceView(APIView):

	def post(self,request,format=None):

		codigo = request.data.get('codigo')
		nome = request.data.get('nome')
		rg = request.data.get('rg')
		cpf = request.data.get('cpf')
		email = request.data.get('email')
		endereco = request.data.get('endereco')

		pessoa = models.Pessoa.objects.create(codigo = codigo, nome = nome, rg = rg, 
			                                         cpf = cpf, email = email, endereco = endereco)

		serializer = serializers.PessoaSerializer(pessoa)
		return Response(serializer.data)



class AtualizarPessoaServiceView(APIView):

	def post(self,request,format=None):

		pessoa = models.Pessoa.objects.get(codigo=request.data.get('codigo'))
		pessoa.nome = request.data.get('nome')
		pessoa.rg = request.data.get('rg')
		pessoa.cpf = request.data.get('cpf')
		pessoa.email = request.data.get('email')
		pessoa.endereco = request.data.get('endereco')

		pessoa.save()

		serializer = serializers.PessoaSerializer(pessoa)
		return Response(serializer.data)




class ExcluirPessoaServiceView(APIView):

	def post(self,request,format=None):

		pessoa = models.Pessoa.objects.get(codigo=request.data.get('codigo'))

		pessoa.delete()

		serializer = serializers.PessoaSerializer(pessoa)
		return Response(serializer.data)


	
