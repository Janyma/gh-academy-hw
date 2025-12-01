# ToDoList API (Django REST Framework)

A simple RESTful API for managing a ToDo list, built with **Django** and **Django REST Framework**.

---

## Features

- View all tasks (`GET /api/tasks/`)
- View a single task (`GET /api/tasks/<id>/`)
- Add a new task (`POST /api/tasks/`)
- Update a task (`PUT/PATCH /api/tasks/<id>/`)
- Delete a task (`DELETE /api/tasks/<id>/`)
- JSON-based API
- Auto-generated API endpoints with Django REST Framework **ViewSets** and **Routers**

---

## Tech Stack

- Python 3.x  
- Django 4.x  
- Django REST Framework (DRF)  
- SQLite (default database)  

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/todolistapi.git
cd todolistapi

### Create a virtual environment

```bash
python -m venv env         # Create venv folder named 'env'
source env/bin/activate     # Linux / Mac
env\Scripts\activate        # Windows


###Install dependencies

```bash
pip install django djangorestframework

###Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate


###Run the development server
```bash
python manage.py runserver


