# Mi Proyecto Django

Una aplicación web moderna en Django con una estructura limpia y organizada.

## 📝 Descripción

Este proyecto sigue una estructura personalizada de directorios:


## 🔍 Requisitos previos

- Python >= 3.7
- Cualquier editor de texto (VSCode, PyCharm, Sublime Text, etc.)

## 🔧 Instalación

Sigue estos pasos para configurar el proyecto:

### 1. Clonar el repositorio

    git clone <url_del_repositorio>
    
    cd <nombre_del_repositorio>  
    

### 2. Crear y activar el entorno virtual

    python3 -m venv venv
    
    source venv/bin/activate

### 3. Instalar las dependencias

    cd src
    
    pip install -r requirements.txt

### 4. Aplicar las migraciones de la base de datos

    python manage.py migrate

### 5. Crear un superusuario

    python manage.py createsuperuser

### 6. Ejecutar el servidor
    cd src
    
    python manage.py runserver

Local: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/
