from django.shortcuts import render, redirect
from .models import Producto, Marca, Categoria
from .forms import ProductoForm


# Vista para la página de inicio
def index(request):
    return render(request, 'index.html')

def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resultado')
    else:
        form = ProductoForm()
    
    return render(request, 'productos/registro.html', {'form': form})

def resultado_producto(request):
    # Obtener el último producto registrado para mostrarlo en la página de resultado
    producto = Producto.objects.last()
    return render(request, 'productos/resultado.html', {'producto': producto})

# Vista para consultar productos con filtros
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
