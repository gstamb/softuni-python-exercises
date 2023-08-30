from django.core.validators import MinLengthValidator
from django.db import models
from plantapp.core.custom_validator import starts_capital_letter

MAX_LEN_UN = 10
MIN_LEN_UN = 2

MAX_LEN_FN = 20

MAX_LEN_LN = 20


class ProfileModel(models.Model):
    username = models.CharField(
        max_length=MAX_LEN_UN,
        blank=False,
        null=False,
        validators=[MinLengthValidator(MIN_LEN_UN), ],
        verbose_name="Username"
    )

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_FN,
        validators=[starts_capital_letter, ],
        verbose_name="First Name"
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_LN,
        validators=[starts_capital_letter, ],
        verbose_name="Last Name"
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name="Profile Picture"
    )
