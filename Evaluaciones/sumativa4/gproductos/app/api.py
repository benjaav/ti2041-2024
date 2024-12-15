from ninja import Router, Schema
from ninja.security import HttpBearer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth.models import User
from app.models import Producto, Marca, Categoria

class TokenSchema(Schema):
    username: str
    password: str

class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            user = User.objects.get(id=user_id)
            return user
        except Exception:
            return None

router = Router()

@router.api_operation(
    path="/categorias/",
    methods=["GET"],
    summary="Listado de Categorías",
    description="Obtiene el listado de todas las categorías registradas.",
    tags=["Categorías"]
)
def listar_categorias(request):
    return list(Categoria.objects.values())

@router.api_operation(
    path="/marcas/",
    methods=["GET"],
    summary="Listado de Marcas",
    description="Obtiene el listado de todas las marcas registradas.",
    tags=["Marcas"]
)
def listar_marcas(request):
    return list(Marca.objects.values())

@router.api_operation(
    path="/productos/",
    methods=["GET"],
    summary="Listado de Productos",
    description="Obtiene el listado de productos con código, nombre y precio. Puede filtrar por marca o categoría.",
    tags=["Productos"]
)
def listar_productos(request, marca: str = None, categoria: str = None):
    productos = Producto.objects.all()
    if marca:
        productos = productos.filter(marca__nombre=marca)
    if categoria:
        productos = productos.filter(categoria__nombre=categoria)
    return list(productos.values("codigo", "nombre", "precio"))

@router.api_operation(
    path="/productos/{codigo}/",
    methods=["GET"],
    summary="Detalle de Producto",
    description="Obtiene el detalle completo de un producto a partir de su código.",
    tags=["Productos"]
)
def detalle_producto(request, codigo: str):
    producto = Producto.objects.filter(codigo=codigo).first()
    if producto:
        return {
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "precio": producto.precio,
            "tamaño": producto.tamaño,
            "marca": producto.marca.nombre,
            "categoria": producto.categoria.nombre,
        }
    return {"error": "Producto no encontrado"}

@router.api_operation(
    path="/productos/{codigo}/",
    methods=["PUT"],
    summary="Actualizar Producto (Completo)",
    description="Actualiza todos los atributos de un producto (nombre, precio, tamaño, marca, categoría) requeridos. Requiere JWT.",
    tags=["Productos"],
    auth=JWTAuth()
)
def actualizar_producto_completo(request, codigo: str, nombre: str, precio: int, tamaño: str, marca: str, categoria: str):
    producto = Producto.objects.filter(codigo=codigo).first()
    if not producto:
        return {"error": "Producto no encontrado"}

    marca_obj = Marca.objects.filter(nombre=marca).first()
    categoria_obj = Categoria.objects.filter(nombre=categoria).first()

    if not marca_obj or not categoria_obj:
        return {"error": "Marca o categoría no válida"}

    producto.nombre = nombre
    producto.precio = precio
    producto.tamaño = tamaño
    producto.marca = marca_obj
    producto.categoria = categoria_obj
    producto.save()
    return {"success": True, "message": "Producto actualizado completamente"}

@router.api_operation(
    path="/productos/{codigo}/",
    methods=["PATCH"],
    summary="Modificar Producto (Parcial)",
    description="Modifica uno o más atributos de un producto. Enviar sólo los campos a modificar. Requiere JWT.",
    tags=["Productos"],
    auth=JWTAuth()
)
def modificar_producto_parcial(request, codigo: str, **kwargs):
    producto = Producto.objects.filter(codigo=codigo).first()
    if not producto:
        return {"error": "Producto no encontrado"}

    if "marca" in kwargs:
        marca_obj = Marca.objects.filter(nombre=kwargs["marca"]).first()
        if not marca_obj:
            return {"error": "Marca no válida"}
        kwargs["marca"] = marca_obj

    if "categoria" in kwargs:
        categoria_obj = Categoria.objects.filter(nombre=kwargs["categoria"]).first()
        if not categoria_obj:
            return {"error": "Categoría no válida"}
        kwargs["categoria"] = categoria_obj

    for key, value in kwargs.items():
        setattr(producto, key, value)

    producto.save()
    return {"success": True, "message": "Producto modificado parcialmente"}

@router.api_operation(
    path="/token/",
    methods=["POST"],
    summary="Obtener Token JWT",
    description="Obtiene un token JWT para autenticar las operaciones que requieren permisos.",
    tags=["Autenticación"]
)
def obtener_token(request, data: TokenSchema):
    user = User.objects.filter(username=data.username).first()
    if user and user.check_password(data.password):
        refresh = RefreshToken.for_user(user)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}
    return {"error": "Credenciales inválidas"}
