from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    CUSTOMER = 'customer', 'Customer'
    ADMIN = 'admin', 'Admin'
    DELIVERY = 'delivery', 'Delivery Boy'


class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.CUSTOMER)
    is_blocked = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'phone']

    def __str__(self) -> str:
        return f'{self.username} ({self.role})'
