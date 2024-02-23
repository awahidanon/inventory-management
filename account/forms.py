
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class CustomUserLoginForm(AuthenticationForm):
    # You can add additional fields or customize the form if needed
    pass

    

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']