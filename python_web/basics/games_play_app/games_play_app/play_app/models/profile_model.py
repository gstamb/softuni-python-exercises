from django.db import models
from django.core.validators import MinValueValidator


class Profile(models.Model):
    MIN_AGE = 12
    AGE_ERR_MSG = "You must be 12 years or older"

    MAX_LEN_PW = 128

    MAX_LEN_NAMES = 30

    email = models.EmailField(
        blank=False,
    )
    age = models.IntegerField(
        blank=False,
        validators=[MinValueValidator(MIN_AGE, AGE_ERR_MSG),]
    )
    password = models.CharField(
        blank=False,
        max_length=MAX_LEN_PW
    )
    first_name = models.CharField(
        blank=True,
        max_length=MAX_LEN_NAMES,
        verbose_name="First Name"
    )
    last_name = models.CharField(
        blank=True,
        max_length=MAX_LEN_NAMES,
        verbose_name='Last Name'
    )
    image_url = models.URLField(
        blank=True,
        verbose_name='Profile Picture'
    )
