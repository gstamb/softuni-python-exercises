from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

USER = 'user'
CUSTOMER = 'customer'
ADMIN = 'admin'


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("role", USER)
        return self._create_user(email, password, **extra_fields)

    def create_customer(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("role", CUSTOMER)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        (USER, 'user'),
        (CUSTOMER, 'customer'),
        (ADMIN, 'admin'),
    ]

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_staff = models.BooleanField(default=False)
    role = models.CharField(
        max_length=50, choices=ROLE_CHOICES, default=USER)

    USERNAME_FIELD = "email"

    objects = UserManager()
