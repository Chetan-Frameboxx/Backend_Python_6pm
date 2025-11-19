# Lecture: Namaste Django

## Theory → Practical Example → Practice Tasks

---

# 1. Theory

## What is Django

Django is a high-level Python web framework used for building secure, scalable, and maintainable web applications. It follows the **MVT (Model–View–Template)** architecture.

### Why Django?

* Fast development
* Built-in authentication
* ORM
* Admin panel
* Secure
* Scalable

---

## MVT Architecture

### Model

Defines the structure of your database tables.

### View

Handles business logic, processes user requests, returns responses.

### Template

HTML files used for presentation.

### Request Flow

```
User → URL → View → Model → View → Template → User
```

---

# 2. Practical Example

**Goal:** Display `Namaste Django` in the browser.

We will build it step-by-step.

---

## Step 1: Create Django Project

```
django-admin startproject myproject
```

---

## Step 2: Use Default manage.py

Do NOT modify manage.py. Correct working version:

```python
#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
```

---

## Step 3: Create App

```
python manage.py startapp namaste_django
```

---

## Step 4: Add App in INSTALLED_APPS

Open **myproject/settings.py** and add:

```python
INSTALLED_APPS = [
    ...
    'namaste_django',
]
```

---

## Step 5: Create a View

Open **namaste_django/views.py**:

```python
from django.http import HttpResponse

def namaste(request):
    return HttpResponse("Namaste Django")
```

---

## Step 6: Create App URLs

Create file **namaste_django/urls.py**:

```python
from django.urls import path
from .views import namaste

urlpatterns = [
    path('', namaste),
]
```

---

## Step 7: Connect App URLs to Project URLs

Open **myproject/urls.py**:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('namaste_django.urls')),
]
```

---

## Step 8: Run Server

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

You will see:

```
Namaste Django
```

---

# 3. Practice Tasks

### Task 1

Create another view that returns:

```
Welcome to Django Learning
```

### Task 2

Create a URL `/hello/` that prints:

```
Hello World from Django
```

### Task 3

Create a URL `/about/` that prints your name.

### Task 4

Create a view that returns today's date.

### Task 5

Create a view returning HTML:

```
<h1>This is a Django HTML Response</h1>
```
