from django.db import models
from django.core.validators import MinLengthValidator


class UserProfile(models.Model):
    MAX_LEN_FN = 25
    MIN_LEN_FN = 2

    MAX_LEN_LN = 35
    MIN_LEN_LN = 1

    MAX_LEN_EMAIL = 40

    MAX_LEN_PW = 20
    MIN_LEN_PW = 8

    DEFAULT_AGE = 18

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_FN,
        validators=(MinLengthValidator(MIN_LEN_FN),)
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_LN,
        validators=(MinLengthValidator(MIN_LEN_LN),)
    )

    email = models.EmailField(
        blank=False,
        null=False,
        max_length=MAX_LEN_EMAIL,
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_PW,
        validators=(MinLengthValidator(MIN_LEN_PW),)
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )

    age = models.IntegerField(
        blank=True,
        null=False,
        default=DEFAULT_AGE
    )
