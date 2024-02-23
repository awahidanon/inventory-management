from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, CustomUserLoginForm

# Create your views here.

class Login(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('index') 


def signup(request):
    
    form = UserCreationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occure during registration')    
   
    return render(request, 'register.html', context )  


def logout_then_login(request, login_url=None):
    """
    Log out the user if they are logged in. Then redirect to the login page.
    """
    login_url = resolve_url(login_url or settings.LOGIN_URL)
    return LogoutView.as_view(next_page=login_url)(request)