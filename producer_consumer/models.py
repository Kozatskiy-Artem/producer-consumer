from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Define a manager for CustomUser model"""

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a new user."""
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a new superuser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("probation", False)
        extra_fields.setdefault("position", 'admin')

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email=email, password=password, **extra_fields)


class CustomUser(AbstractUser):
    probation = models.BooleanField(default=True)
    position = models.CharField(max_length=50)

    objects = CustomUserManager()
    REQUIRED_FIELDS: list[str] = ['email']


class Order(models.Model):
    task_id = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
