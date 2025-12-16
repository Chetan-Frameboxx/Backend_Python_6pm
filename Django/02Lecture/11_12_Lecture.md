# Session 11 & 12 — Class-Based Views (CBVs), CRUD & Advanced ORM

---

## THEORY

### 1. Class-Based Views (CBVs)

**What are CBVs?**
CBVs are Django views implemented as Python classes. They promote reusability, cleaner code, and built-in behaviors for common patterns like listing, creating, updating, and deleting data.

#### CBVs vs FBVs

| Feature       | FBVs                   | CBVs                        |
| ------------- | ---------------------- | --------------------------- |
| Structure     | Function-based         | Class-based                 |
| Reusability   | Limited                | High (inheritance & mixins) |
| Built-in CRUD | Manual                 | Provided by Django          |
| Readability   | Simple for small logic | Cleaner for large apps      |

---

### 2. Common Built-in CBVs

* **ListView** – Display list of objects
* **DetailView** – Display single object
* **CreateView** – Create new object
* **UpdateView** – Update existing object
* **DeleteView** – Delete object

Each CBV works with a Django **Model** and **Template** by convention.

---

### 3. Customizing CBVs

You can customize CBVs using:

* `model`
* `template_name`
* `context_object_name`
* `fields`
* Overriding methods:

  * `get_queryset()`
  * `form_valid()`
  * `get_context_data()`

---

### 4. Mixins

**Mixins** add extra behavior to CBVs.

Common mixins:

* `LoginRequiredMixin` – restrict access to logged-in users
* `PermissionRequiredMixin` – permission-based access
* `UserPassesTestMixin` – custom access logic

---

### 5. CRUD Using CBVs

CRUD = Create, Read, Update, Delete

CBVs provide **complete CRUD** with minimal code using:

* CreateView
* ListView
* DetailView
* UpdateView
* DeleteView

---

### 6. Advanced ORM Concepts

#### a) `select_related`

* Used for **ForeignKey**
* Performs SQL JOIN
* Improves performance

#### b) `prefetch_related`

* Used for **ManyToMany / reverse FK**
* Executes separate queries and joins in Python

---

### 7. Q Objects

Used for **complex queries** with OR, AND, NOT logic.

---

### 8. F Expressions

Used to compare or update model fields **without fetching data into Python**.

---

### 9. Aggregations & Annotations

* **Aggregation** – Summary values (Count, Sum, Avg, Min, Max)
* **Annotation** – Add calculated fields to each object

---

## PRACTICAL EXAMPLES (FULL PROGRAMS)

### Model Example

```python
# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name
```

---

### ListView

```python
# views.py
from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
```

---

### DetailView

```python
from django.views.generic import DetailView

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
```

---

### CreateView

```python
from django.views.generic import CreateView
from django.urls import reverse_lazy

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'stock']
    success_url = reverse_lazy('product_list')
```

---

### UpdateView

```python
from django.views.generic import UpdateView

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['price', 'stock']
    success_url = reverse_lazy('product_list')
```

---

### DeleteView

```python
from django.views.generic import DeleteView

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
```

---

### LoginRequiredMixin

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class SecureProductListView(LoginRequiredMixin, ListView):
    model = Product
```

---

### select_related Example

```python
Product.objects.select_related('category').all()
```

---

### prefetch_related Example

```python
Product.objects.prefetch_related('tags').all()
```

---

### Q Objects

```python
from django.db.models import Q

Product.objects.filter(Q(price__gt=500) | Q(stock__lt=10))
```

---

### F Expressions

```python
from django.db.models import F

Product.objects.update(stock=F('stock') - 1)
```

---

### Aggregation

```python
from django.db.models import Avg

Product.objects.aggregate(avg_price=Avg('price'))
```

---

### Annotation

```python
from django.db.models import Count

Product.objects.annotate(total=models.Count('id'))
```

---

## PRACTICE TASKS

### CBVs & CRUD

1. Create a Student model and implement full CRUD using CBVs.
2. Protect Create, Update, Delete views using `LoginRequiredMixin`.
3. Customize `get_queryset()` to show only active records.

### ORM Practice

4. Use `Q` objects to filter products with price > 1000 OR stock < 5.
5. Use `F` expression to increase all prices by 10%.
6. Display average price and total product count using aggregation.
7. Annotate each product with total number of orders.

---

