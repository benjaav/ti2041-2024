from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from app.api import router as productos_router
from app import views

api = NinjaAPI(
    title="API de Productos",
    description="API RESTFul para administrar productos, categorías y marcas. Incluye autenticación JWT para modificación.",
)

api.add_router("/", productos_router) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registro/', views.registrar_producto, name='registro'),
    path('consulta/', views.consulta_productos, name='consulta'),
    path('resultado/', views.resultado_producto, name='resultado'),
    path('index/', views.index, name='index'),

    path("api/", api.urls),  
]
