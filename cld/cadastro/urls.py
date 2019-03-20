from django.urls import path

from . import views 


urlpatterns =[
    path('index',views.index,name='index'), 
    path('',views.cadastro_list,name='cadastro_list'),
    path('cadastro/<int:pk>/',views.cadastro_detail,name='cadastro_detail'), 
    path('cadastro/new/',views.cadastro_new,name='cadastro_new'), 
    path('cadastro/<int:pk>/edit/', views.cadastro_edit, name='cadastro_edit'), 
    path('cadastro/<int:pk>/delete/', views.cadastro_delete, name='cadastro_delete'),
]