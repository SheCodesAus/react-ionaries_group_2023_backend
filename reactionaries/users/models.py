from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False)
    email = models.EmailField(max_length=254, unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


# Create your models here.
