# Lecture 8: Flask Blueprints and Project Structure

## Theory

### 1. Why Modularization?

As Flask applications grow larger, keeping all routes and logic in a single `app.py` file becomes hard to manage. To solve this, Flask provides **Blueprints** — a way to organize the app into smaller, modular components.

### 2. What is a Blueprint?

A **Blueprint** is a logical collection of routes, templates, and static files grouped together as a mini-application.

They make your project:

* Easier to maintain
* More organized
* Easier to collaborate on (different modules can be developed independently)

### 3. Benefits of Using Blueprints

* **Separation of concerns:** Keep related routes and logic together.
* **Reusability:** Blueprints can be reused across multiple projects.
* **Scalability:** Suitable for large or enterprise-level applications.

### 4. Registering Blueprints

After creating a Blueprint, it must be registered in the main application.

```python
from flask import Flask
from user.routes import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/user')
```

Here, all routes inside `user_bp` will start with `/user`.

### 5. Application Factory Pattern

Instead of creating the Flask app directly in `app.py`, we define a function that returns a configured app instance.
This allows:

* Easier testing and configuration management.
* Creating multiple instances of the app if needed.

Example:

```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    from user.routes import user_bp
    app.register_blueprint(user_bp)

    return app
```

---

## Practical Example

**Objective:**
Refactor the Task Manager App using Blueprints and an application factory structure.

### 📁 Folder Structure

```
task_manager/
│
├── run.py
├── task_manager/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   └── tasks.html
│   └── static/
│       └── style.css
│
└── instance/
    └── task_manager.db
```

### File: `run.py`

```python
from task_manager import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

### File: `task_manager/__init__.py`

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'
    app.config['SECRET_KEY'] = 'mysecretkey'

    db.init_app(app)

    from task_manager.routes import main
    app.register_blueprint(main)

    return app
```

### File: `task_manager/routes.py`

```python
from flask import Blueprint, render_template, request, redirect, url_for
from .models import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('tasks.html')
```

### File: `task_manager/models.py`

```python
from . import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
```

### File: `task_manager/templates/base.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Task Manager</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Task Manager</h1>
    {% block content %}{% endblock %}
</body>
</html>
```

### File: `task_manager/templates/tasks.html`

```html
{% extends 'base.html' %}
{% block content %}
    <p>Welcome to Task Manager (Blueprint version)!</p>
{% endblock %}
```

---

## Practice Task

**Task:**
Refactor your previous Task Manager App to use:

* A Blueprint for task-related routes (`tasks_bp`).
* A separate Blueprint for authentication (`auth_bp`).
* The application factory pattern for initializing the app.

**Expected Output:**

* Organized folder structure.
* Modular app with independent route files.
* Task Manager runs successfully with Blueprints.
