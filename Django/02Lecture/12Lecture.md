# Practical Project — Product Inventory Management System (CBVs & Advanced ORM)

---

## PROJECT OVERVIEW

In this project, you will build a **Product Inventory Management System** using **Django Class-Based Views (CBVs)** and **Advanced ORM concepts**.

This project is designed to practically apply:

* CBVs vs FBVs
* ListView, DetailView, CreateView, UpdateView, DeleteView
* Custom CBVs
* Mixins (LoginRequiredMixin)
* Complete CRUD
* Advanced ORM (select_related, prefetch_related, Q, F)
* Aggregations & Annotations

---

## MODULES COVERED

* Session 11: CBVs & Mixins
* Session 12: CRUD & Advanced ORM

---

## FEATURES

* Authentication-based access
* Product CRUD using CBVs
* Category-wise product management
* Optimized database queries
* Inventory stock management
* Analytics dashboard

---

## PROJECT FOLDER STRUCTURE

```
inventory_project/
│
├── manage.py
│
├── inventory_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── products/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── tests.py
│
├── templates/
│   ├── base.html
│   └── products/
│       ├── list.html
│       ├── detail.html
│       ├── form.html
│       └── confirm_delete.html
│
├── static/
│   └── css/
│       └── style.css
│
└── db.sqlite3
```

---

## inventory_project/settings.py (Important Settings)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
]

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

---

## inventory_project/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
]
```

---

## products/models.py

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

---

## products/admin.py

```python
from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
```

---

## products/views.py (CBVs)

```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q, F, Avg, Sum
from .models import Product, Category

class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('category')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'category', 'price', 'stock']
    success_url = reverse_lazy('product_list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['price', 'stock']
    success_url = reverse_lazy('product_list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
```

---

## products/urls.py

```python
from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', ProductCreateView.as_view(), name='product_add'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
```

---

## templates/base.html

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Inventory System</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <h1>Product Inventory Management</h1>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>

```

---

## templates/products/list.html

```html
{% extends 'base.html' %}
{% block content %}
<a href="{% url 'product_add' %}">Add Product</a>
<ul>
{% for product in products %}
    <li>
        <a href="{% url 'product_detail' product.id %}">{{ product.name }}</a>
    </li>
{% endfor %}
</ul>
{% endblock %}
```

---

## templates/products/detail.html

```html
{% extends 'base.html' %}
{% block content %}
<h2>{{ object.name }}</h2>
<p>Category: {{ object.category }}</p>
<p>Price: {{ object.price }}</p>
<p>Stock: {{ object.stock }}</p>
<a href="{% url 'product_edit' object.id %}">Edit</a>
<a href="{% url 'product_delete' object.id %}">Delete</a>
{% endblock %}
```

---
## templates/products/form.html

```html
{% extends 'base.html' %}

{% block content %}
<h2>{{ view.object|default:'Add Product' }}</h2>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}

    <button type="submit">Save</button>
    <a href="{% url 'product_list' %}">Cancel</a>
</form>
{% endblock %}
```

---
## templates/products/confirm_delete.html

```html
{% extends 'base.html' %}

{% block content %}
<h2>Confirm Delete</h2>

<p>Are you sure you want to delete <strong>{{ object.name }}</strong>?</p>

<form method="post">
    {% csrf_token %}
    <button type="submit">Yes, Delete</button>
    <a href="{% url 'product_list' %}">Cancel</a>
</form>
{% endblock %}

```
---
## static/css/style.css

```css
/* Reset & Base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

body {
    background-color: #f4f6f8;
    padding: 20px;
    color: #333;
}

/* Headings */
h1 {
    margin-bottom: 15px;
    color: #2c3e50;
}

h2 {
    margin-bottom: 10px;
    color: #34495e;
}

/* Links */
a {
    text-decoration: none;
    color: #3498db;
    margin-right: 10px;
}

a:hover {
    text-decoration: underline;
}

/* Buttons */
button {
    padding: 8px 14px;
    background-color: #3498db;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #2980b9;
}

/* Forms */
form {
    background: #fff;
    padding: 15px;
    margin-top: 10px;
    border-radius: 6px;
    max-width: 400px;
}

form p {
    margin-bottom: 10px;
}

input, select {
    width: 100%;
    padding: 6px;
    margin-top: 4px;
}

/* List */
ul {
    list-style: none;
    margin-top: 10px;
}

ul li {
    background: #fff;
    padding: 10px;
    margin-bottom: 6px;
    border-radius: 4px;
}

/* Confirmation box */
p {
    margin: 10px 0;
}


```

---

## ADVANCED ORM USAGE (Examples)

```python
Product.objects.filter(Q(price__gt=1000) | Q(stock__lt=5))
Product.objects.update(stock=F('stock') - 1)
Product.objects.aggregate(avg_price=Avg('price'), total_stock=Sum('stock'))
Category.objects.annotate(product_count=models.Count('products'))
```

---

## LEARNING OUTCOME

After completing this project, you will be able to:

* Build full CRUD using CBVs
* Secure views using Mixins
* Optimize database queries
* Use advanced Django ORM confidently

---

### END OF PRACTICAL PROJECT
