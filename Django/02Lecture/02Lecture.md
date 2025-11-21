# Session 2 — Migrations, Database & Superuser

## Theory

### What Are Migrations?

Migrations in Django are a way to propagate changes made to your models (Python classes) into the database structure. Whenever you create or update models, migrations keep the database schema in sync with the code.

### Why Are Migrations Needed?

* To create database tables
* To modify table structure when models change
* To track changes over time
* To keep database and models consistent

---

## Database in Django

Django uses SQLite by default (a lightweight file‑based database). The database configuration is found in `settings.py` under `DATABASES`.

Default configuration:

```python\DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

You can replace this with MySQL/PostgreSQL if needed.

---

## Commands for Migrations

### 1. Create Migration Files

```bash
python manage.py makemigrations
```

This scans all apps for model changes and prepares migration files.

### 2. Apply Migrations to Database

```bash
python manage.py migrate
```

This updates the database schema using migration files.

### 3. Check Migration Status

```bash
python manage.py showmigrations
```

Shows which migrations are applied and which are pending.

---

## Creating Superuser

Superuser is an admin-level user who can log into Django Admin.

Command:

```bash
python manage.py createsuperuser
```

You will be asked for:

* Username
* Email (optional)
* Password

Once created, you can log in at:

```
http://127.0.0.1:8000/admin
```

---

## Practical Example (As Taught in a Real Class)

### Step 1: Create a Model

Open `models.py` in your app:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
```

### Step 2: Make Migrations

```bash
python manage.py makemigrations
```

Output:

```
Migrations for 'school':
  school/migrations/0001_initial.py
      - Create model Student
```

### Step 3: Apply Migrations

```bash
python manage.py migrate
```

### Step 4: Register Model in Admin

Open `admin.py`:

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

### Step 5: Create Superuser

```bash
python manage.py createsuperuser
```

Login to `/admin` and test Student model CRUD.

---

## Practice Tasks

### Task 1

Create a model named `Employee` with the following fields:

* name
* department
* salary
* join_date

Run migrations and make it visible in Django Admin.

### Task 2

Create a second app and add a new model. Perform migrations and check if both apps show tables in the database.

### Task 3

Modify an existing model by adding a new field (e.g., `email`). Then:

* Run `makemigrations`
* Run `migrate`
  Observe how Django updates the table.

---

