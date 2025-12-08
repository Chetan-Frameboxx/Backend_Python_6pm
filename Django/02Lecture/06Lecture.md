# Session 7 — Forms & ModelForms

## 1. Theory

### Django Form Class

Django provides a powerful `forms.Form` class that helps you create HTML forms in Python. Instead of manually writing HTML inputs, Django generates them automatically.

A form handles:

* Rendering fields in HTML
* Validating input
* Showing validation errors
* Converting input to Python types
* Cleaning data

### Why Use Django Forms?

* Automatic validation
* Security against invalid input
* Clean and maintainable code
* Saves development time

### Validation in Forms

Validation runs when you call:

```python
form.is_valid()
```

If the form is valid:

* `form.cleaned_data` contains clean data.

If invalid:

* `form.errors` contains error messages.

Types of validation:

* Built‑in validation
* Field‑level validation (`clean_<field>()`)
* Form‑level validation (`clean()`)

### ModelForms

A `ModelForm` is a form built from a Django model.

Advantages:

* Auto‑generated fields from model
* Can save to database directly with `form.save()`
* Reduces code duplication

### Error Handling in Forms

When validation fails, Django stores errors in:

```python
form.errors
```

Errors can be:

* Field-specific
* Non‑field errors (general form errors)

### Showing Errors in Templates

You can show errors using:

```html
{{ form.non_field_errors }}
{{ form.field_name.errors }}
{{ form.errors }}
```

Or show everything automatically:

```html
{{ form.as_p }}
```

---

## 2. Practical Examples (Full Programs)

### Example 1 — Simple Django Form

#### forms.py

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name cannot contain numbers.")
        return name
```

#### views.py

```python
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            return render(request, "success.html", {"data": cleaned})

    return render(request, "contact.html", {"form": form})
```

#### contact.html

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}

    {% if form.errors %}
        <div style="color:red;">
            {{ form.errors }}
        </div>
    {% endif %}

    <button type="submit">Submit</button>
</form>
```

---

### Example 2 — ModelForm (Insert into Database)

#### models.py

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
```

#### forms.py

```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'age']
```

#### views.py

```python
from django.shortcuts import render
from .forms import StudentForm

def student_create(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")

    return render(request, "student_form.html", {"form": form})
```

#### student_form.html

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}

    {% if form.errors %}
        <div style="color:red;">
            {{ form.errors }}
        </div>
    {% endif %}

    <button type="submit">Save</button>
</form>
```

---

### Example 3 — Showing Errors Field‑by‑Field

```html
<p>
    {{ form.name.label_tag }}
    {{ form.name }}
    <span style="color:red;">{{ form.name.errors }}</span>
</p>
<p>
    {{ form.email.label_tag }}
    {{ form.email }}
    <span style="color:red;">{{ form.email.errors }}</span>
</p>
<p>
    {{ form.age.label_tag }}
    {{ form.age }}
    <span style="color:red;">{{ form.age.errors }}</span>
</p>
```

---

## 3. Practice Tasks

### Task 1 — Create a Login Form

Fields:

* username
* password

Validation:

* Username must be at least 4 characters
* Password must not be "1234"

Show field-wise errors.

### Task 2 — Build a Feedback ModelForm

Model fields:

* name
* email
* feedback (minimum 20 characters)

### Task 3 — Create a Registration Form

Fields:

* name
* email
* password
* confirm password

Validation:

* Passwords must match
* Email must be a Gmail address

### Task 4 — Insert Student Data & Display It

Use ModelForm to insert data and show all records in a table.

### Task 5 — Add Custom Error Message

Implement:

```python
error_messages={'required': 'This field cannot be empty'}
```
