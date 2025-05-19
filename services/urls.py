from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('providers/', views.provider_list, name='provider_list'),
    path('register/', views.register_provider, name='register_provider'),  # ✅ THIS LINE
]
