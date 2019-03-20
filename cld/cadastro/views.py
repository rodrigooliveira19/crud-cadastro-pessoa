from django.shortcuts import render
from django.http import HttpResponse
from . models import Pessoa
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PessoaForm

from . import urls

# Create your views here.


def index(request):
	return HttpResponse("<strong>Olá, Mundo. Você está acessando a página index de cadastro.</strong>")


def cadastro_list(request):
	pessoas = Pessoa.objects.order_by('nome')
	return render(request,'cadastro/cadastro_list.html',{'pessoas':pessoas})


def cadastro_detail(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    return render(request, 'cadastro/cadastro_detail.html', {'pessoa': pessoa})


def cadastro_new(request):
	if request.method =="POST":
		form = PessoaForm(request.POST)
		if form.is_valid():
			pessoa = form.save(commit=False)
			pessoa.save()
			return redirect('cadastro_detail',pk=pessoa.pk)
	else:
		form = PessoaForm()
	return render(request,'cadastro/cadastro_edit.html',{'form':form})



def cadastro_edit(request,pk):
	pessoa = get_object_or_404(Pessoa,pk=pk) 
	if request.method == "POST":
		form = PessoaForm(request.POST,instance=pessoa)
		if form.is_valid():
			pessoa = form.save(commit=False)
			pessoa.save()
			return redirect('cadastro_detail',pk=pessoa.pk)
	else:
		form = PessoaForm(instance=pessoa)
	return render(request,'cadastro/cadastro_edit.html',{'form':form})



def cadastro_delete(request,pk):
	pessoa = get_object_or_404(Pessoa,pk=pk)
	if request.method =="POST":
		pessoa.delete()
		return redirect('cadastro_list')
	else:
		form = PessoaForm(instance=pessoa)
	return render(request,'cadastro/cadastro_delete.html',{'pessoa':pessoa})