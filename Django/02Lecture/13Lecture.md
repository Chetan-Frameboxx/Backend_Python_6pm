# Session 13 — Django Signals & Middleware

---

## 1. Theory

### 1.1 Django Signals

Django signals allow certain senders to notify a set of receivers when specific actions occur. They help in **decoupling** logic so that different parts of an application can react to events without being tightly connected.

Common built-in model signals:

* **pre_save** – triggered just before a model’s `save()` method is executed
* **post_save** – triggered after a model is saved
* **pre_delete** – triggered before a model instance is deleted
* **post_delete** – triggered after deletion

Key concepts:

* **Sender**: The model or component that sends the signal
* **Receiver**: A function that runs when the signal is triggered
* **Signal dispatcher**: Manages connections between senders and receivers

Why signals exist:

* To keep models and views clean
* To avoid duplicating logic across the project
* To respond automatically to lifecycle events

### 1.2 pre_save Signal

* Runs **before** data is saved to the database
* Useful for:

  * Auto-generating values (slug, code, timestamps)
  * Data validation or normalization
  * Modifying fields before persistence

Important note:

* The instance is **not yet saved**, so no primary key may exist

### 1.3 post_save Signal

* Runs **after** the object is saved
* Provides a `created` flag to detect first-time creation

Useful for:

* Creating related objects (profiles, logs)
* Sending emails or notifications
* Updating analytics or audit tables

### 1.4 When Signals Are Used in Real Systems

Real-world use cases:

* Creating a **UserProfile** automatically when a user registers
* Logging activity whenever data is updated
* Sending email/SMS after order creation
* Updating search indexes

When NOT to use signals:

* When logic is critical and must be explicit
* When debugging becomes difficult due to hidden side effects
* When order of execution matters strictly

Rule of thumb:

> Use signals for **side effects**, not for core business logic

### 1.5 Django Middleware

Middleware is a framework of hooks into Django’s **request/response processing**.

Middleware is a class that can:

* Process a request before it reaches the view
* Process a response before it is returned to the client

Middleware sits between:

Client → Middleware → View → Middleware → Response

### 1.6 Common Uses of Middleware

* Authentication and authorization
* Logging requests and responses
* Measuring performance
* Modifying request/response objects
* Blocking or redirecting requests

### 1.7 Request/Response Lifecycle

1. Client sends HTTP request
2. Django loads middleware (top to bottom)
3. Middleware `process_request` runs
4. URL routing happens
5. View function/class executes
6. Middleware `process_response` runs (bottom to top)
7. Response sent back to client

Order matters in middleware execution.

---

## 2. Practical Examples (Full Programs)

### 2.1 pre_save Signal Example

**models.py**

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
```

**signals.py**

```python
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Product

@receiver(pre_save, sender=Product)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
```

**apps.py**

```python
from django.apps import AppConfig

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        import products.signals
```

### 2.2 post_save Signal Example

**models.py**

```python
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
```

**signals.py**

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

### 2.3 Custom Middleware Example

**middleware.py**

```python
import time

class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        print(f"Request took {end_time - start_time} seconds")
        return response
```

**settings.py**

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'yourapp.middleware.RequestTimeMiddleware',
]
```

### 2.4 Middleware Modifying Response

```python
class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-App-Name'] = 'InventorySystem'
        return response
```

---

## 3. Practice Tasks

### Signals Practice

1. Create a `pre_save` signal to automatically capitalize a user’s name.
2. Use `post_save` to create a log entry whenever a product is updated.
3. Add a signal to send a welcome email after user registration.
4. Prevent saving a model if a certain condition is not met using `pre_save`.
5. Create a signal that updates stock history after an order is placed.

### Middleware Practice

6. Create middleware to log IP address of each request.
7. Write middleware to block requests after office hours.
8. Add middleware to count total requests handled by the server.
9. Create middleware that redirects unauthenticated users.
10. Modify response headers to add application version.

### Conceptual Questions

11. Difference between `pre_save` and `post_save`.
12. Why should signals not contain core business logic?
13. Explain middleware execution order.
14. How does middleware differ from decorators?
15. What problems arise from excessive use of signals?

---

### Summary

* Signals help react to model lifecycle events
* `pre_save` modifies data before persistence
* `post_save` handles side effects after saving
* Middleware controls request/response flow
* Proper use improves scalability and maintainability
