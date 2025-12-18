# Practical Project — Product Inventory Management System

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

## DATABASE DESIGN

### Category Model

```python
# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

### Product Model

```python
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

## CBV IMPLEMENTATION

### Product ListView (select_related)

```python
# views.py
from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('category')
```

---

### Product DetailView

```python
from django.views.generic import DetailView

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
```

---

### Create Product (LoginRequiredMixin)

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'category', 'price', 'stock']
    success_url = reverse_lazy('product_list')
```

---

### Update Product

```python
from django.views.generic import UpdateView

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['price', 'stock']
    success_url = reverse_lazy('product_list')
```

---

### Delete Product

```python
from django.views.generic import DeleteView

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
```

---

## ADVANCED ORM USAGE

### Q Objects (Filtering)

```python
from django.db.models import Q

Product.objects.filter(Q(price__gt=1000) | Q(stock__lt=5))
```

---

### F Expressions (Stock Update)

```python
from django.db.models import F

Product.objects.filter(id=1).update(stock=F('stock') - 1)
```

---

### Aggregation (Dashboard Stats)

```python
from django.db.models import Avg, Sum

Product.objects.aggregate(avg_price=Avg('price'), total_stock=Sum('stock'))
```

---

### Annotation (Product Count per Category)

```python
from django.db.models import Count

Category.objects.annotate(product_count=Count('products'))
```

---

## URL CONFIGURATION

```python
# urls.py
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

## PRACTICE EXTENSIONS

1. Add search functionality using Q objects.
2. Add pagination to ProductListView.
3. Restrict delete access to superusers only.
4. Create a dashboard page using annotations.
5. Add prefetch_related for future order relations.

---

## LEARNING OUTCOME

After completing this project, you will confidently:

* Build real-world CRUD apps using CBVs
* Optimize ORM queries
* Implement authentication-based access
* Use Django ORM like a professional

---

### END OF PRACTICAL PROJECT



# Installation Steps

## 1. Create virtual environment
python -m venv env

## 2. Activate virtual environment
### Windows
env\Scripts\activate

# macOS / Linux
source env/bin/activate

## 3. Install Django
pip install django

## 4. Create Django project
django-admin startproject inventory_project
cd inventory_project

## 5. Create app
python manage.py startapp products

## 6. Register app in settings.py
```
INSTALLED_APPS = [
    ...
    'products',
]
```

## 7. Apply migrations
python manage.py makemigrations
python manage.py migrate

## 8. Create admin user
python manage.py createsuperuser

## 9. Run server
python manage.py runserver


## Project Folder Structure
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
│   ├── models.py        # Category & Product models
│   ├── views.py         # CBVs (List, Create, Update, Delete)
│   ├── urls.py          # App-level URLs
│   ├── forms.py         # Optional (custom forms)
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