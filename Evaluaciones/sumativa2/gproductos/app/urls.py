from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio
    path('registro/', views.registrar_producto, name='registro'),
    path('resultado/', views.resultado_producto, name='resultado'),
    path('consulta/', views.consulta_productos, name='consulta'),
]
