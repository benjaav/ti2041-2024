# ti2041-2024
# Gestión de Productos en Django

Este proyecto es una aplicación web construida con Django que permite a los usuarios registrar productos, consultar la lista de productos registrados, y ver detalles del último producto registrado. Esta aplicación es ideal para pequeñas empresas o proyectos educativos que necesitan un sistema básico de gestión de inventarios.

## Características

- **Registro de productos**: Permite ingresar productos con detalles como código, nombre, marca y fecha de vencimiento.
- **Consulta de productos**: Muestra una lista de todos los productos registrados en el sistema.
- **Visualización de último producto registrado**: Permite ver los detalles del último producto ingresado al sistema.

## Tecnologías Utilizadas

- **Django**: Framework web para el desarrollo rápido de aplicaciones seguras y mantenibles.
- **SQLite**: Base de datos utilizada para el almacenamiento local de datos.

## Instalación y Configuración

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/benjaav/ti2041-2024/tree/main/Evaluaciones/sumativa1/gproductos
   cd gestion-productos-django
2. Crear un entorno virtual e instalar las dependencias

3. Configurar las variables de entorno

4. Realizar las migraciones de base de datos

5. Ejecutar el servidor local

**instalar dependencias**
pip install -r requirements.txt

**aplicar migraciones**
python manage.py makemigrations
python manage.py migrate


**iniciar el servidor de desarrollo**
cd .\gproductos
python manage.py runserver
Esto iniciará un servidor local en http://localhost:8000/.


