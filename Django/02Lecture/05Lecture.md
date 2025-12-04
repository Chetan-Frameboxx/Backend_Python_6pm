# Lecture: Working with Forms in Django

## 1. Theory

### What Are Forms in Django?

Forms allow users to submit data to the server. Django provides a powerful **forms framework** that helps with:

* Rendering HTML forms
* Validating input
* Handling GET & POST requests
* Preventing security issues (e.g., CSRF attacks)

---

### GET vs POST Method

#### GET Method

* Used to request data from the server.
* Data is visible in the URL.
* Safe for read-only actions.

Example GET URL:

```
/add?num1=5&num2=10
```

#### POST Method

* Used to send data securely to the backend.
* Data is **not shown** in the URL.
* Used for form submissions, login, signup, etc.

---

### CSRF Token

When using POST requests in Django templates you must include:

```
{% csrf_token %}
```

To prevent Cross-Site Request Forgery attacks.

---

### Flow of Django Form Submission

1. User visits a page with a form (GET request).
2. User fills the form and submits (POST request).
3. Django receives the data in `request.POST`.
4. Backend processes the data.
5. Backend returns a response or redirects to another page.

---

## 2. Practical Examples (Full Programs)

### Example 1: Displaying a Simple Form using GET (Addition)

**urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_numbers, name='add_numbers'),
]
```

**views.py**

```python
def add_numbers(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    result = None

    if num1 and num2:
        result = int(num1) + int(num2)

    return render(request, 'add.html', {'result': result})
```

**add.html**

```html
<h2>Add Two Numbers (GET Method)</h2>
<form method="GET">
    <input type="number" name="num1" placeholder="Enter number 1" required>
    <input type="number" name="num2" placeholder="Enter number 2" required>
    <button type="submit">Add</button>
</form>

{% if result %}
<p>Result: {{ result }}</p>
{% endif %}
```

---

### Example 2: POST Form Submission (Sending Data to Another Page)

**urls.py**

```python
urlpatterns = [
    path('form/', views.form_page, name='form_page'),
    path('result/', views.result_page, name='result_page'),
]
```

**views.py**

```python
from django.shortcuts import render, redirect

def form_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        return redirect('result_page')

    return render(request, 'form_page.html')

def result_page(request):
    return render(request, 'result_page.html')
```

**form_page.html**

```html
<h2>Submit Your Details (POST Method)</h2>
<form method="POST">
    {% csrf_token %}
    <input type="text" name="name" placeholder="Enter your name" required>
    <input type="number" name="age" placeholder="Enter your age" required>
    <button type="submit">Submit</button>
</form>
```

**result_page.html**

```html
<h2>Form Submitted Successfully</h2>
<p>Data received and processed.</p>
```

---

### Example 3: Simple Addition Using POST Method

**views.py**

```python
def add_post(request):
    result = None
    if request.method == 'POST':
        n1 = int(request.POST.get('n1'))
        n2 = int(request.POST.get('n2'))
        result = n1 + n2

    return render(request, 'add_post.html', {'result': result})
```

**add_post.html**

```html
<h2>Add Two Numbers (POST Method)</h2>
<form method="POST">
    {% csrf_token %}
    <input type="number" name="n1" placeholder="Enter number 1" required>
    <input type="number" name="n2" placeholder="Enter number 2" required>
    <button type="submit">Add</button>
</form>

{% if result %}
<p>Result: {{ result }}</p>
{% endif %}
```

---

## 2.4 Example: GET + POST Workflow with Redirect (Real Use Case)

### views.py

```python
def ticket(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request, "ticket.html", {'output': output})


def userForm(request):
    result = 0
    data = {}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            result = n1 + n2

            data = {
                'n1': n1,
                'n2': n2,
                'output': result
            }

            url = ('/ticket?output={}'.format(result))
            return redirect(url)
    except:
        pass

    return render(request, "userform.html", data)
```

### userform.html

```html
{% extends "base.html" %}
{% block content %}
<div class="ticket-section ">
    <div class="container mt-5 py-5 border border-1 text-bg-dark">
        <form method="post">
            {% csrf_token %}
            <div>
                <label class="form-label">Value 1</label>
                <input type="text" name="num1" value="{{n1}}" class="form-control">
            </div>
            <div>
                <label class="form-label">Value 2</label>
                <input type="text" name="num2" value="{{n2}}" class="form-control">
            </div>
            <div>
                <button type="submit" class="btn btn-primary my-3">Submit</button>
            </div>
            <div>
                <input type="text" value="{{output}}">
            </div>
        </form>
    </div>
</div>
{% endblock %}
```

### ticket.html

```html
{% extends "base.html" %}
{% block content %}
<h2>Redirect Output Page</h2>
<p>Result: {{ output }}</p>
{% endblock %}
```

This example demonstrates:

* Reading POST data
* Performing backend computation
* Redirecting with GET parameters
* Displaying result on another page (ticket.html)

## 3. Practice Tasks

### Task 1

Create a GET-based calculator with 4 operations:

* Addition
* Subtraction
* Multiplication
* Division

### Task 2

Build a POST form that collects:

* Name
* Email
* Phone
* Message
  And displays the full data on a new page.

### Task 3

Create a POST addition form that redirects to another page and shows the result with the following message:

```
The sum of X and Y is Z
```

### Task 4

Create a Django form (using Django's `forms.Form`) that validates:

* Name should not be empty
* Age should be above 18
* Email should be valid

---

End of Lecture
