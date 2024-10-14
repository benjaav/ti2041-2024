from django.shortcuts import render, redirect

# Estructura en memoria para almacenar productos
productos_registrados = []

# Vista para el registro de productos
def registrar_producto(request):
    if request.method == "POST":
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')

        # Crear un diccionario para representar un producto
        producto = {
            'codigo': codigo,
            'nombre': nombre,
            'marca': marca,
            'fecha_vencimiento': fecha_vencimiento
        }

        # Guardar el producto en la lista
        productos_registrados.append(producto)

        # Redirigir a la vista de resultado
        return redirect('resultado')

    return render(request, 'productos/registro.html')

# Vista para mostrar el producto recién registrado
def resultado_producto(request):
    ultimo_producto = productos_registrados[-1] if productos_registrados else None
    return render(request, 'productos/resultado.html', {'producto': ultimo_producto})

# Vista para mostrar todos los productos registrados
def consulta_productos(request):
    return render(request, 'productos/consulta.html', {'productos': productos_registrados})

def index(request):
    return render(request, 'index.html')
