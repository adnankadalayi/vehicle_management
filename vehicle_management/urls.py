from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('superadmin/', include('superadmin.urls')),
    path('admin_panel/', include('admin_panel.urls')),
    path('', include('user.urls')),
]
