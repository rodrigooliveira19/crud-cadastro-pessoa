from django import forms

from .models import Pessoa


#Padrão de formulario para cadastrar pessoa. 
class PessoaForm(forms.ModelForm):

	class Meta:
		model = Pessoa
		fields = ('codigo', 'nome', 'rg', 'cpf', 'email', 'endereco',)