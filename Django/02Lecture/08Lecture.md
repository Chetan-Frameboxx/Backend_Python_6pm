# Django Project: Forms + Static + Media + File Upload

> Single-file markdown guide + full folder structure you can copy-paste.

---

## Project Overview

This example creates a small Django project (`mysite`) with an app `accounts` that demonstrates:

* A form for **username, password, email, phone number**
* Static files (CSS/JS/images)
* Media uploads (user avatar)
* File uploads (documents)

It uses:

* Django `Form` and `ModelForm`
* `ImageField` and `FileField`
* `static` and `media` configuration for development

---

## Folder Structure

```
mysite/
├── manage.py
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── accounts/
│   │   │   ├── register.html
│   │   │   ├── upload.html
│   │   │   └── profile_list.html
│   └── migrations/
├── static/
│   └── css/
│       └── style.css
└── media/
    ├── avatars/
    └── documents/
```

---

## Requirements

* Python 3.8+
* Django (tested with 4.x)

Install:

```bash
python -m venv venv
source venv/bin/activate   # mac/linux
venv\Scripts\activate     # windows
pip install django
django-admin startproject mysite
cd mysite
python manage.py startapp accounts
```

---

## `mysite/settings.py` (important parts)

```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]},
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

---

## `mysite/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),

    # IMPORTANT: include accounts app URLs
    path('', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## `accounts/models.py`

```python
from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.username

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

## `accounts/forms.py`

```python
from django import forms
from .models import Profile, Document

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)

    def clean_username(self):
        u = self.cleaned_data.get('username')
        if len(u) < 4:
            raise forms.ValidationError('Username must be at least 4 characters')
        return u

    def clean_password(self):
        pw = self.cleaned_data.get('password')
        if pw == '1234':
            raise forms.ValidationError('Password too weak')
        return pw

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'phone', 'avatar']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']

    def clean_file(self):
        f = self.cleaned_data.get('file')
        if f:
            # simple size check (example)
            if f.size > 5 * 1024 * 1024:
                raise forms.ValidationError('File too large ( > 5MB )')
            return f
```

---

## `accounts/views.py`

```python
from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileModelForm, DocumentForm
from .models import Profile, Document

def register_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # You may want to create a Profile model instance or a real User
            Profile.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone']
            )
            return redirect('profile_list')
    return render(request, 'accounts/register.html', {'form': form})



def profile_create_view(request):
    form = ProfileModelForm()
    if request.method == 'POST':
        form = ProfileModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    return render(request, 'accounts/create_profile.html', {'form': form})


def profile_list(request):
    data = Profile.objects.all()
    return render(request, 'accounts/profile_list.html', {'profiles': data})


def upload_document(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('documents')
    return render(request, 'accounts/upload.html', {'form': form})


def documents(request):
    docs = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'accounts/documents.html', {'docs': docs})
```

---

## `accounts/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('create-profile/', views.profile_create_view, name='create_profile'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.documents, name='documents'),
]
```

---

## Templates

### `templates/accounts/register.html`

```html
{% load static %}
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Register</title>
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
  <h1>Register (Form)</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
  </form>
</body>
</html>
```
### `templates/accounts/create-profile.html`

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Create Profile</title>
</head>
<body>

<h1>Create Profile (ModelForm)</h1>

<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}

    <button type="submit">Save Profile</button>
</form>

</body>
</html>

```

### `templates/accounts/upload.html`

```html
{% load static %}
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Upload Document</title>
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
  <h1>Upload Document</h1>
  <form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
  </form>
</body>
</html>
```

### `templates/accounts/profile_list.html`

```html
{% load static %}
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Profiles</title>
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
  <h1>Profiles</h1>
  {% for p in profiles %}
    <div class="profile">
      <p>{{ p.username }} — {{ p.email }} — {{ p.phone }}</p>
      {% if p.avatar %}
        <img src="{{ p.avatar.url }}" alt="avatar" width="80">
      {% endif %}
    </div>
  {% endfor %}
</body>
</html>
```

### `templates/accounts/documents.html`

```html
{% load static %}
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Documents</title>
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
  <h1>Documents</h1>
  <ul>
    {% for d in docs %}
      <li><a href="{{ d.file.url }}">{{ d.title }}</a> — {{ d.uploaded_at }}</li>
    {% endfor %}
  </ul>
</body>
</html>
```

---

## Static file example: `static/css/style.css`

```css
body { font-family: Arial, sans-serif; padding: 20px; }
.profile { margin-bottom: 12px; }
```

---

## Admin (optional)

Register models in `accounts/admin.py`:

```python
from django.contrib import admin
from .models import Profile, Document

admin.site.register(Profile)
admin.site.register(Document)
```

---

## Run the project

1. Make migrations & migrate:

```bash
python manage.py makemigrations
python manage.py migrate
```

2. Create superuser (optional):

```bash
python manage.py createsuperuser
```

3. Run server:

```bash
python manage.py runserver
```

4. Browse:

* [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)  (form)
* [http://127.0.0.1:8000/create-profile/](http://127.0.0.1:8000/create-profile/) (ModelForm with avatar)
* [http://127.0.0.1:8000/profiles/](http://127.0.0.1:8000/profiles/)  (list)
* [http://127.0.0.1:8000/upload/](http://127.0.0.1:8000/upload/)  (file upload)
* [http://127.0.0.1:8000/documents/](http://127.0.0.1:8000/documents/) (list uploaded files)

---

## Notes & Tips

* In production, serve static & media through your web server (Nginx/Cloud storage).
* Install `Pillow` to support `ImageField`:

  ```bash
  pip install pillow
  ```
* Add validation rules as needed (file types, max size, phone format).
* If you want username/password tied to Django `User`, use `UserCreationForm` and link `Profile` with `OneToOneField` to `auth.User`.

---

