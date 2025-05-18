from django.contrib.auth.models import User
from django.db import models

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.service_type}"
