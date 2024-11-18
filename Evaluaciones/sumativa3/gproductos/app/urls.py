from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),  
    path('logout/', views.logout_user, name='logout'),
    path('registro/', views.registrar_producto, name='registro'),
    path('consulta/', views.consulta_productos, name='consulta'),
    path('resultado/', views.resultado_producto, name='resultado'),
    path('index/', views.index, name='index'), 
]


