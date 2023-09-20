from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Define a manager for CustomUser model"""

    def create_user(self, email, username, first_name, last_name, password, **extra_fields):
        """Create and return a new user."""
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password, **extra_fields):
        """Create and return a new superuser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("probation", False)
        extra_fields.setdefault("position", 'admin')

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )


class CustomUser(AbstractUser):
    probation = models.BooleanField(default=True)
    position = models.CharField(max_length=50)

    objects = CustomUserManager()
    REQUIRED_FIELDS = ['email']


class Order(models.Model):
    task_id = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
