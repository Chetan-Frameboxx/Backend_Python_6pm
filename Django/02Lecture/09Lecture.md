# Session 9 & 10 — User Authentication (Complete Module)

---

# **Session 9 — User Authentication (Part 1)**

## **1. Introduction to Django Authentication System**

Django provides a powerful built-in authentication system that handles:

* Users
* Password hashing
* Login/logout
* Sessions
* Permissions

---

## **2. Signup (User Registration)**

To allow users to create accounts, we generally use Django’s built-in `User` model.

### **Key Concepts**

* `User.objects.create_user()` ensures password hashing
* Validation handled by Django auth system

### **Basic Signup Workflow**

1. User submits registration form
2. Form validates username/email/password
3. User is saved (password is hashed)
4. Redirect to login page

---

## **3. Login Workflow**

### **Steps**

* User enters username + password
* Django uses `authenticate()` to verify credentials
* If valid → `login(request, user)` stores user session
* Redirect to dashboard/home

---

## **4. Logout Workflow**

Uses Django’s built‑in `logout(request)` function.

Call logout → session clears → user logged out.

---

## **5. Password Hashing**

Django **never stores raw passwords**.

It uses hashing algorithms like:

* PBKDF2 (default)
* Argon2
* BCrypt

Passwords are always saved using:

```python
user = User.objects.create_user(username, email, password)
```

---

## **6. Restricting Views using `login_required`**

To prevent anonymous access:

```python
from django.contrib.auth.decorators import login_required

@login_required

def dashboard(request):
    return render(request, "dashboard.html")
```

Anonymous users → redirect to login URL.

---

# **Session 10 — User Authentication (Part 2)**

## **1. Custom User Model (Introduction)**

When the default `User` model is not enough, Django allows:

### **Two Main Approaches**

1. **AbstractUser** (recommended) – extends default User
2. **AbstractBaseUser** – fully custom user system

### **Why Create Custom User Model?**

* Add mobile number
* Add user types (student, admin, teacher)
* Replace username with email login

---

## **2. User Profile Model**

A common pattern is extending the default User with a Profile:

```
User (auth_user)
      ↓ OneToOne
Profile (extra fields)
```

Allows storing:

* Avatar
* Phone number
* Address
* DOB
* User type

---

## **3. Password Reset Flow (Email)**

Django provides a complete password-reset workflow:

### **Includes:**

* Forgot password page
* Reset email sending
* Secure token-based link
* New password form

### **Steps:**

1. User enters email
2. Django sends reset link
3. User opens link → new password page
4. New password saved in hashed form

---

## **4. Permissions & Groups**

Django comes with powerful permission control.

### **Permissions**

* Add
* Change
* Delete
* View

Each model gets these permissions automatically.

### **Groups**

A group is a collection of permissions.
You assign users to groups → they automatically get permissions.

### **Use‑cases**

* **Admins** can add/edit/delete users
* **Managers** can edit but not delete
* **Students** can only view

---

# **Summary (Sessions 9 & 10)**

| Feature                | Session    |
| ---------------------- | ---------- |
| Signup/Login/Logout    | Session 9  |
| Password Hashing       | Session 9  |
| Restrict Views         | Session 9  |
| Custom User Model      | Session 10 |
| User Profile Model     | Session 10 |
| Reset Password (Email) | Session 10 |
| Permissions & Groups   | Session 10 |

---

