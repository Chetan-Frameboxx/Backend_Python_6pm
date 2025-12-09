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