from api_rest import views 
from django.urls import path 



urlpatterns =[
    path('pessoas/', views.PessoaListServiceView.as_view(),name='pessoas'),
    path('cadastrarPessoa/', views.CadastrarPessoaServiceView.as_view(),name='cadastrarPessoa'), 
    path('atualizarPessoa/', views.AtualizarPessoaServiceView.as_view(),name='atualizarPessoa'),
    path('excluirPessoa/', views.ExcluirPessoaServiceView.as_view(),name='excluirPessoa'),  
]