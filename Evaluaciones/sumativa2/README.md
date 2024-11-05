# Gestión de Productos

Este proyecto es una aplicación web desarrollada con Django para gestionar productos, específicamente zapatillas. Permite registrar, consultar y filtrar productos, con categorías, marcas, tamaños y precios.

## Características

- Registrar productos con atributos como: **nombre**, **marca**, **categoría**, **tamaño** y **precio**.
- Consultar productos registrados y filtrarlos por **marca** y **categoría**.
- Interfaz de usuario estilizada con **CSS**.
- Validación de datos en el formulario de registro.
- Implementación de funcionalidades de Django como vistas, modelos y formularios.

## Requisitos

- **Python 3.11+**
- **Django 4.x**

## Instalación

1. Instala las dependencias del proyecto: pip install -r requirements.txt
2. Realiza las migraciones para configurar la base de datos: python manage.py migrate
3. Crea un superusuario para acceder al panel de administración de Django: python manage.py createsuperuser
4. Inicia el servidor de desarrollo: python manage.py runserver
5. Accede a la aplicación desde tu navegador en http://127.0.0.1:8000/.

 

## Estructura del Proyecto
app/: Contiene los archivos principales de la aplicación, incluyendo modelos, vistas y formularios.
static/: Contiene los archivos estáticos como el CSS.
templates/: Contiene las plantillas HTML del proyecto.
gproductos/: Configuración general del proyecto Django.

## Archivos importantes
models.py: Define los modelos para Producto, Marca, Categoría.
views.py: Contiene las vistas para el registro y consulta de productos.
urls.py: Define las rutas de las páginas de la aplicación.
templates/productos: Carpeta donde se encuentran las plantillas HTML (index.html, registro.html, consulta.html, resultado.html).

