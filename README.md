💻 My Django Project
A modern Django web application with a clean, organized structure.

📃 Overview
This project follows a custom structure:

src/: Main code directory
config/: Project configuration
core/: Main application
venv/: Virtual environment (not tracked in git)
🔍 Prior Requirements
Python >= 3.7
Any text editor
🔧 Instalation
Follow these steps to create a project using Django:

Clone this repository

Create and activate virtual environment

python -m venv venv
.\venv\Scripts\activate
If .\venv\Scripts\activate use this code first Set-ExecutionPolicy Unrestricted -Scope Process. This allows the use of scripts in the system.

Install dependencies

cd src
pip install -r requirements.txt
Apply migrations

python manage.py migrate
Create a superuser

python manage.py createsuperuser
🚀 Running the project
    cd src
    python manage.py runserver
Access the site at http://127.0.0.1:8000/ and admin at http://127.0.0.1:8000/admin/
