from django.db import models
from django.contrib.auth.models import AbstractUser




# ------------------ Custom User ------------------
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"

    role = models.CharField(max_length=20, choices=Role.choices,default=Role.USER)
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True)
    level = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} - {self.last_name})"

