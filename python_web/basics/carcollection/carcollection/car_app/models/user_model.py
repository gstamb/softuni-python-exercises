from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    MIN_LEN_UN = 2
    MIN_AGE = 18
    MAX_AGE = 150
    MAX_LEN_FN = 30
    MAX_LEN_LN = 30
    MAX_LEN_PW = 128

    username = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        validators=[
            MinLengthValidator(MIN_LEN_UN, f"The username must be a minimum of {MIN_LEN_UN} chars")
        ],
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(MAX_AGE, "It is not safe to drive"),
            MinValueValidator(MIN_AGE, f"You must be of age to register")
        ]
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_PW
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_LEN_FN,
        verbose_name="First Name"

    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_LEN_LN,
        verbose_name="Last Name"

    )

    image_url = models.URLField(
        blank=True,
        null=False,
        verbose_name="Profile Picture"
    )
