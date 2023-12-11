from django.db import models
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
# Create your models here.

class UserWithRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=CustomUserCreationForm.ROLE_CHOICES)