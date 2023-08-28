from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator

def name_start_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!",
                              params={'value': value}
                              )


class UserProfile(models.Model):
    first_name = models.CharField(
        blank=False, max_length=25)
    last_name = models.CharField(
        blank=False, max_length=35)
    email = models.EmailField(
        blank=False, max_length=40)
    password = models.CharField(
        blank=False, max_length=20)
    image_url = models.URLField(blank=True)
    age = models.IntegerField(blank=True, default=18)

