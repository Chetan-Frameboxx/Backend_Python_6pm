# Practical Project — Django Authentication


* Custom User Model
* Signup with Avatar & Phone
* Login / Logout
* Password Reset (Email Flow)
* Permissions & Groups
* Admin‑Only Views
* Correct Template Paths
* Correct URL Structure
* Correct MEDIA settings

---

# 1. Project Structure

```
namasteapp/
├── newaccounts/
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   └── newaccounts/
│   │       ├── signup.html
│   │       ├── login.html
│   │       ├── profile.html
│   ├── templates/
│   │   └── registration/
│   │       ├── password_reset_form.html
│   │       ├── password_reset_done.html
│   │       ├── password_reset_confirm.html
│   │       ├── password_reset_complete.html
├── namasteapp/
│   ├── settings.py
│   ├── urls.py
├── media/
└── manage.py
```

---

# 2. Custom User Model

## newaccounts/models.py

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.username
```

## settings.py

```python
AUTH_USER_MODEL = 'newaccounts.CustomUser'
```

---

# 3. Signup Form

## newaccounts/forms.py

```python
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'avatar']
```

---

# 4. Signup View (Corrected Template Path)

## newaccounts/views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'newaccounts/signup.html', {'form': form})
```

---

# 5. Login, Logout, Profile View

```python
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

@login_required
def profile_view(request):
    return render(request, 'newaccounts/profile.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')
```

---

# 6. Password Reset (Corrected Template Structure)

## settings.py

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Django searches for password reset templates in:

```
/templates/registration/
```

### newaccounts/urls.py

```python
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='newaccounts/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Password reset flow
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
```

---

# 7. Permissions & Groups

## Django Shell Setup

```python
from django.contrib.auth.models import Group, Permission

admin_group = Group.objects.create(name='AdminGroup')
manager_group = Group.objects.create(name='ManagerGroup')

perm = Permission.objects.get(codename='view_user')
admin_group.permissions.add(perm)
```

## Protect Views

```python
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.groups.filter(name='AdminGroup').exists()

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'newaccounts/admin_dashboard.html')
```

---

# 8. Templates (Corrected)

## signup.html

```html
<h2>Create Account</h2>
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Sign up</button>
</form>
```

---

# 9. Project-Level URLs

## namasteapp/urls.py

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newaccounts.urls')),    # Correct
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

# 10. MEDIA Settings (Required for Avatar Upload)

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

# 11. Final Output (What Your Project Supports)

* Custom User Model (username, email, phone, avatar)
* Signup with Image Upload
* Login & Logout
* Profile Page
* Password Reset Flow
* Permissions & Groups
* Admin‑Only Views (Role Based)


