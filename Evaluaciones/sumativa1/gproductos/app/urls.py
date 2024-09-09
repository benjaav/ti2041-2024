from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resultado', views.resultado, name='resultado'),
    path('registro', views.registro, name='registro'),
    path('consulta', views.consulta, name='consulta'),
]

