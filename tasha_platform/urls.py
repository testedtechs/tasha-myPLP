from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('services.urls')),   # Home page
    path('accounts/', include('accounts.urls')),  # Auth routes
]
