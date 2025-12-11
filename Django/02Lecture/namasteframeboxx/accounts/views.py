# from django.shortcuts import render, redirect
# from .forms import RegistrationForm, ProfileModelForm, DocumentForm
# from .models import Profile, Document



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import user_passes_test
from .forms import CustomUserCreationForm


# Create your views here.

# def register_view(request):
#     form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # You may want to create a Profile model instance or a real User
#             Profile.objects.create(
#                 username=form.cleaned_data['username'],
#                 email=form.cleaned_data['email'],
#                 phone=form.cleaned_data['phone']
#             )
#             return redirect('profile_list')
#     return render(request, 'accounts/register.html', {'form': form})



# def profile_create_view(request):
#     form = ProfileModelForm()
#     if request.method == 'POST':
#         form = ProfileModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('profile_list')
#     return render(request, 'accounts/create_profile.html', {'form': form})


# def profile_list(request):
#     data = Profile.objects.all()
#     return render(request, 'accounts/profile_list.html', {'profiles': data})


# def upload_document(request):
#     form = DocumentForm()
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('documents')
#     return render(request, 'accounts/upload.html', {'form': form})


# def documents(request):
#     docs = Document.objects.all().order_by('-uploaded_at')
#     return render(request, 'accounts/documents.html', {'docs': docs})



# new 


# -----------------------------
# Signup
# -----------------------------
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


# -----------------------------
# Profile Page
# -----------------------------
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


# -----------------------------
# Logout
# -----------------------------
def logout_view(request):
    auth_logout(request)
    return redirect('login')


# -----------------------------
# Admin Dashboard
# -----------------------------
def is_admin(user):
    return user.groups.filter(name='AdminGroup').exists()


@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')