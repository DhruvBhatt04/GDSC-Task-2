# orders/models.py
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    priority = models.CharField(max_length=20)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional user profile fields if needed
