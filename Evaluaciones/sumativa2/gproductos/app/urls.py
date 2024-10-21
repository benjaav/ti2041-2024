from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registrar_producto, name='registro'),
    path('consulta/', views.consulta_productos, name='consulta'),
    path('resultado/', views.resultado_producto, name='resultado'),  # Esta es la vista que faltaba
]
