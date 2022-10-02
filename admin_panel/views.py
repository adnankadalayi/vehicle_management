from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from superadmin.forms import VehicleForm

from superadmin.models import Vehicle

def admin_panel(request):
    if request.user.is_authenticated:
        vehicle = Vehicle.objects.all()
        context = {
            'vehicle': vehicle,
        }
        return render(request, 'admin_panel/home.html', context)
    return redirect('admin_login')


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('admin_home')
        messages.error(request,"You are not Admin or Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/login.html', context)
        
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

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

