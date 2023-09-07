from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.


class Profile(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    email = models.EmailField(blank=False)

    age = models.IntegerField(blank=True, null=True, validators=[
                              MinValueValidator(0)],)
    