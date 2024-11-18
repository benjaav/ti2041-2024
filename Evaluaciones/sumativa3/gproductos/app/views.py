from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto, Marca, Categoria
from .forms import ProductoForm

def is_admin(user):
    return user.is_superuser
# Vista para el login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'productos/login.html')  

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resultado')
    else:
        form = ProductoForm()
    
    return render(request, 'productos/registro.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def resultado_producto(request):
    # Obtener el último producto registrado para mostrarlo en la página de resultado
    producto = Producto.objects.last()
    return render(request, 'productos/resultado.html', {'producto': producto})

# Vista para consultar productos con filtros
@login_required
def consulta_productos(request):
    productos = Producto.objects.all()
    marca_id = request.GET.get('marca')
    categoria_id = request.GET.get('categoria')

    if marca_id:
        productos = productos.filter(marca_id=marca_id)

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    return render(request, 'productos/consulta.html', {
        'productos': productos,
        'marcas': marcas,
        'categorias': categorias,
    })
