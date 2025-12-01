# 4 — Django Views & Templates (Part 1 & 2)

## Theory

## Session 3 — Views & Templates (Part 1)

### 1. Function-Based Views

* A function in `views.py` that handles request and returns a response.

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django")
```

### 2. Rendering HTML Templates

* Use `render()` to load HTML from templates folder.

```python
from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")
```

### 3. Passing Data to Templates

```python
def home(request):
    context = {
        'title': 'Welcome Page',
        'message': 'Learning Django Templates'
    }
    return render(request, "core/home.html", context)
```

### 4. Jinja Template Syntax (Django Template Language)

* **Variables**: `{{ value }}`
* **Conditions**:

```html
{% if logged_in %}
   Welcome User
{% endif %}
```

* **Loops**:

```html
{% for item in items %}
   <p>{{ item }}</p>
{% endfor %}
```

---

## Session 4 — Views & Templates (Part 2)

### 5. Template Inheritance

Reuse a base layout across pages.

`base.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Website</h1>
    </header>

    {% block content %}
    {% endblock %}
</body>
</html>
```

### 6. Using `extends` and `block`

Child template:

```html
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
<h2>Welcome Home</h2>
<p>This page uses inheritance.</p>
{% endblock %}
```

### 7. Template Filters

Django provides built-in filters to transform data.
Examples:

* `{{ name|upper }}`
* `{{ date|date:"d M Y" }}`
* `{{ text|truncatewords:10 }}`

### 8. Template Reuse Patterns

* **Include reusable parts**:

```html
{% include 'components/navbar.html' %}
```

* **Common patterns**:

  * Reusable navbars
  * Reusable cards
  * Shared footers
  * Modular template blocks

---

## Practical Examples

### Example 1 — Passing Data

```python
# core/views.py

def about(request):
    context = {
        'username': 'Chetan',
        'skills': ['Django', 'Python', 'SQL'],
    }
    return render(request, 'core/about.html', context)
```

```html
<!-- core/templates/core/about.html -->
<h1>Hello {{ username }}</h1>
<ul>
{% for skill in skills %}
    <li>{{ skill }}</li>
{% endfor %}
</ul>
```

### Example 2 — Using Base Template

```html
<!-- core/templates/core/home.html -->
{% extends 'base.html' %}

{% block content %}
<h2>Dashboard</h2>
<p>Welcome to the app.</p>
{% endblock %}
```

---

## Practice Tasks

1. Create a base template with header & footer.
2. Make two child pages (`home.html` and `contact.html`) that extend the base.
3. Add a reusable navbar using `{% include %}`.
4. Use filters to display:

   * username in uppercase
   * truncate a long text into 15 words
   * format current date
5. Create a list of products in view and display them using Jinja loops.
