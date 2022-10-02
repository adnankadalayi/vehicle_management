from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from superadmin.models import Vehicle

from user.forms import UserCreateForm

def home(request):
    if request.user.is_authenticated:
        vehicle = Vehicle.objects.all()
        context = {
            'vehicle': vehicle,
        }
        return render(request, 'user/home.html', context)
    return redirect('user_login')

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('user_home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'user/signup.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('user_home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('user_home')
        messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'user/login.html', context)
        
def user_logout(request):
    logout(request)
    return redirect('user_login')
