# Session 1 — Introduction & Setup

## 1. Theory

### What is Django

Django is a high-level Python web framework designed for rapid, secure, and scalable web development. It follows the MVT architecture and provides tools such as ORM, admin panel, authentication, and routing.

### MVT Architecture (Model–View–Template)

#### Model

Represents the database structure and data handling.

#### View

Contains application logic and interacts with the Model. It sends data to the Template.

#### Template

Handles the presentation layer using HTML files.

#### Request Flow

User → URL → View → Model → View → Template → User

---

## 2. Installing Django and Virtual Environment

### Create Virtual Environment

```
python -m venv env
```

### Activate Virtual Environment

Windows:

```
env\Scripts\activate
```

Linux/Mac:

```
source env/bin/activate
```

### Install Django

```
pip install django
```

### Check Django Version

```
django-admin --version
```

---

## 3. Starting a Django Project

### Create Project

```
django-admin startproject myproject
```

---

## 4. Project Folder Structure

```
myproject/
│
├── manage.py
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

### Important Files

* manage.py — Command-line utility for project operations.
* settings.py — Configuration for the Django project.
* urls.py — Maps URLs to views.
* wsgi.py/asgi.py — Deployment interfaces.

---

## 5. Running the Development Server

### Run Server

```
python manage.py runserver
```

### Custom Port

```
python manage.py runserver 8080
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## Practical Examples

### Example: Create a Project

```
django-admin startproject shop
```

### Example: Run Server

```
cd shop
python manage.py runserver
```

### Example: Change Port

```
python manage.py runserver 9000
```

---

## Practice Tasks

1. Create a virtual environment and install Django.
2. Create a Django project named `learningportal`.
3. Explore each file in the project folder and write a one-line explanation.
4. Run the development server on default and custom ports.
5. Deactivate and reactivate the virtual environment.



# Django Theory: What is Django & MVT Architecture

## Theory

### What is Django

Django is a high-level Python web framework designed for rapid, secure, and scalable web development. It provides built-in components such as ORM, admin panel, authentication system, URL routing, and template engine. Django follows the **MVT (Model–View–Template)** architectural pattern, which helps developers structure applications cleanly and efficiently.

---

## MVT Architecture (Model–View–Template)

### Model

Defines the structure of the database and manages all data-related operations. Models represent the data layer of a Django application.

### View

Contains the business logic. Views receive requests, interact with models, process data, and send responses to templates.

### Template

Responsible for the presentation layer. Templates define how data is displayed using HTML files.

### Request Flow

```
User → URL → View → Model → View → Template → User
```
