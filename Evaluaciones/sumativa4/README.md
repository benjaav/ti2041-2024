# ti2041-2024
# Gestión de Productos en Django

Este proyecto es una API RESTFul desarrollada en Django con NinjaAPI. Permite administrar un catálogo de productos, incluyendo categorías y marcas, y brindar servicios para listar, filtrar, obtener detalles y modificar productos. Además, incluye un sistema de autenticación JWT para asegurar las operaciones que requieren permisos.

**Requerimientos**
Python
Django 
NinjaAPI
djangorestframework-simplejwt

**instalacion y Configuracion**
1.- clonar el repositorio
bash
Copiar código
git clone <url_del_repositorio> evaluaciones/sumativa4

2.-Instalar dependencias
pip install -r requirements.txt

3.- Migraciones de la base de datos
python manage.py migrate


**Estructura del Proyecto**
-gproductos/
-settings.py, urls.py, etc.: Configuración principal del proyecto.
-productos/ (Aplicación requerida)
-models.py: Definición de modelos Categoria, Marca, Producto.
-api.py: Implementación de la API usando NinjaAPI.
-views.py: Vistas base (opcional, mayormente para interfaz web).
-forms.py: Formularios (opcional para interfaz web).
-admin.py: Registro de modelos en el administrador de Django.

**Endpoints de la API**

La API se basa en NinjaAPI. Todos los servicios están disponibles bajo la ruta /api/.

-Listado de Categorías (GET)
GET /api/categorias/
Retorna todas las categorías.

-Listado de Marcas (GET)
GET /api/marcas/
Retorna todas las marcas.

-Listado de Productos (GET)
GET /api/productos/

-Detalle de un Producto (GET)
GET /api/productos/1/
Retorna todos los atributos del producto identificado por codigo.

-Modificar un Producto (PUT)
PUT /api/productos/{codigo}/
Actualiza todos los atributos del producto (nombre, precio, tamaño, marca, categoría).
Requiere Autenticación JWT.

-Modificar un Producto (PATCH)
PATCH /api/productos/{codigo}/
Modifica algunos atributos del producto (parcial).
Requiere Autenticación JWT.

-Obtener Token JWT (POST)
POST /api/token/
Body (JSON):

{
  "username": "editor",
  "password": "inacap2024"
}
Retorna refresh y access token. El access token debe ser utilizado en las peticiones protegidas, agregando el header Authorization: Bearer 

**Autenticación JWT**
1.- Obtener el token:
curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"editor": "admin", "password": "inacap2024"}'

respuesta:
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}

2.-Utilizar el token en peticiones PUT/PATCH:
curl -X PATCH http://127.0.0.1:8000/api/productos/1/ \
-H "Authorization: Bearer <access_token>" \
-H "Content-Type: application/json" \
-d '{"precio": 2500}'
(Si el token es válido, la modificación se aplica correctamente. Sin token, se devuelve un error de autorización.)


**Documentación de la API**
La documentación generada automáticamente por NinjaAPI (Swagger/OpenAPI) se encuentra en:
http://127.0.0.1:8000/api/docs

Allí se podra ver cada endpoint, sus parámetros, y probarlos directamente.
