from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileModelForm, DocumentForm
from .models import Profile, Document

# Create your views here.

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