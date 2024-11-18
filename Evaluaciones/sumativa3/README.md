## **Características**
- Registro de productos con nombre, categoría, marca, tamaño y precio.
- Consulta de productos registrados con filtros.
- Autenticación de usuarios para restringir el acceso a las funcionalidades.
- Vista y template para el inicio de sesión (login).
- Cierre de sesión (logout).
- Acceso exclusivo para administradores en ciertas funcionalidades.
- Aplicación de un diseño básico utilizando CSS como archivo estático.

---

## **Requisitos Previos**
Antes de instalar y ejecutar esta aplicación, asegúrate de contar con:
- Python 3.11 o superior.
- Django 5.1 instalado.
- Una terminal o entorno de desarrollo configurado (VS Code, PyCharm, etc.).
- Git instalado para clonar y administrar el repositorio.

---

## **Instalación**
1. **Clonar el Repositorio:**
   git clone https://github.com/<benjaav>/evaluaciones.git
   cd evaluaciones/sumativa3

## **Crear un Entorno Virtual:**
python -m venv env
env\Scripts\activate  # En Windows


**Instalar Dependencias:**

pip install django
**Configurar la Base de Datos:**
Ejecuta las migraciones para configurar la base de datos:
python manage.py makemigrations
python manage.py migrate

**Ejecución**

Iniciar el Servidor: Inicia el servidor local con:

Copiar código
python manage.py runserver
**Acceso a la Aplicación**
: Abre tu navegador e ingresa la URL:
http://127.0.0.1:8000


**Uso de la Aplicación**
Pantalla de Inicio:

Los usuarios no autenticados verán un enlace para iniciar sesión.
Los usuarios autenticados podrán registrar productos, consultar productos y ver el último producto registrado.
**Login:**

Ingresa tus credenciales en http://127.0.0.1:8000/login/.
**Logout:**
Cierra sesión con el enlace correspondiente en la barra de navegación o directamente accediendo a http://127.0.0.1:8000/logout/.
Protección de Funcionalidades:
Todas las vistas importantes requieren autenticación.
la vista de resultado está restringidas solo para administradores.


**Protección y Restricciones**
Autenticación:
El decorador @login_required protege las vistas de registro, consulta y resultados.
Restricción de Administradores:
El decorador @user_passes_test(lambda u: u.is_superuser) restringe la vista resultados.



**usuario Normal sin permisos de admin**
nombre: benjita
password: Santana2004