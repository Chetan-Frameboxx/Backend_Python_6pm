# Session 2 & 3 — Django Apps, URLs, Views & Templates

## Theory

### 1. Creating Django Apps

* A Django **project** contains multiple **apps**.
* Each app represents a module: blog, accounts, shop, etc.
* Command to create an app:

```
python manage.py startapp appname
```

* Inside the app folder you get models.py, views.py, apps.py, admin.py, etc.

### 2. URL Routing in Django

Django uses URL patterns to map URLs to views.

* All URLs start from `project/urls.py`.
* Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

### 3. Project-level vs App-level URLs

**Project-level URLs:**

* Located in `projectname/urls.py`.
* Main entry point that includes URLs of all apps.

**App-level URLs:**

* Each app can have its own `urls.py` for better structure.
* Then included in project URLs.

### 4. Including Multiple Apps

Add multiple apps inside project URLs:

```python
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
]
```

---

## Session 3 — Views & Templates (Part 1)

### 5. Function-Based Views

A simple function-based view:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django")
```

### 6. Rendering HTML Templates

Use `render()` to load a template:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

Templates go inside:

```
appname/templates/appname/home.html
```

### 7. Passing Data to Templates

```python
def home(request):
    data = {
        'title': 'Django Tutorial',
        'message': 'Welcome to Templates'
    }
    return render(request, 'home.html', data)
```

### 8. Jinja Template Syntax

Django template language (DTL) supports:

* Variables: `{{ variable }}`
* Conditions:

```html
{% if user %}
   Hello {{ user }}
{% endif %}
```

* Loops:

```html
{% for item in items %}
   <p>{{ item }}</p>
{% endfor %}
```

---

## Practical Examples

### Example 1: Project-level URL

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

### Example 2: App-level URL

```python
# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

### Example 3: Template Rendering

```python
# core/views.py
from django.shortcuts import render

def home(request):
    context = {'title': 'Home Page'}
    return render(request, 'core/home.html', context)
```

```html
<!-- core/templates/core/home.html -->
<h1>{{ title }}</h1>
```

---

## Practice Tasks

1. Create a new app called **accounts** and show "Login Page" using a function-based view.
2. Add project-level and app-level URLs for the **accounts** app.
3. Create a template that displays a list of 5 items passed from the view.
4. Use Jinja loop in the template to print the items.
5. Create two apps (**blog**, **shop**) and include them in the project URLs.
