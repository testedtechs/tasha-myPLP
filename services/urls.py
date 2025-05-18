from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]


from .views import register_provider

urlpatterns += [
    path('register-provider/', register_provider, name='register_provider'),
]
