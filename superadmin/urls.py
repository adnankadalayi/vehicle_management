from django.urls import path
from . import views

urlpatterns = [
    path('', views.superadmin, name='superadmin_home'),
    path('login', views.superadmin_login, name='superadmin_login'),
    path('logout', views.superadmin_logout, name='superadmin_logout'),
    path('add-vehicle', views.add_vehicle, name='add_vehicle'),
    path('edit-vehicle/<int:id>', views.edit_vehicle, name='edit_vehicle'),
    path('delete-vehicle/<int:id>', views.delete_vehicle, name='delete_vehicle'),
]
