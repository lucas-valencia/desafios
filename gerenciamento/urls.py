# gerenciamento/urls.py

from django.urls import path
#from .views import index, cadastro, consulta, editar_cliente, apagar_cliente
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('consulta/', views.consulta, name='consulta'),
    path('editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('apagar/<int:cliente_id>/', views.apagar_cliente, name='apagar_cliente'),

]