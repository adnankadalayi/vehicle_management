from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from superadmin.forms import VehicleForm

from superadmin.models import Vehicle

def superadmin(request):
    if request.user.is_authenticated:
        vehicle = Vehicle.objects.all()
        context = {
            'vehicle': vehicle,
        }
        return render(request, 'superadmin/home.html', context)
    return redirect('superadmin_login')


def superadmin_login(request):
    if request.user.is_authenticated:
        return redirect('superadmin_home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('superadmin_home')
        messages.error(request,"You are not Superadmin or Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'superadmin/login.html', context)
        
def superadmin_logout(request):
    logout(request)
    return redirect('superadmin_login')

def add_vehicle(request):
    
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('superadmin_home')
    form  = VehicleForm()
    context = {
        'form': form,
    }
    return render(request, 'superadmin/add_vehicle.html', context)

def edit_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('superadmin_home')
    form  = VehicleForm(instance=vehicle)
    context = {
        'form': form,
    }
    return render(request, 'superadmin/edit_vehicle.html', context)

def delete_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    vehicle.delete()
    return redirect('superadmin_home')
