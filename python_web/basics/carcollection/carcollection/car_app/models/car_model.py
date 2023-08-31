from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models


class Car(models.Model):
    CAR_TYPE_MAX_LEN = 10

    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2

    YEAR_MANUFACTURED_MIN_VAL = 1980
    YEAR_MANUFACTURED_MAX_VAL = 2049
    YEAR_MANUFACTURED_ERR_MSG = f"Year must be between {YEAR_MANUFACTURED_MIN_VAL} and {YEAR_MANUFACTURED_MAX_VAL}"

    SPORTS_CAR = 'Sports Car'
    PICKUP_TRUCK = 'Pickup'
    CROSSOVER_SUV = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'
    DEFAULT = '----------'

    CAR_TYPES = [
        (SPORTS_CAR, 'Sports Car'),
        (PICKUP_TRUCK, 'Pickup'),
        (CROSSOVER_SUV, 'Crossover'),
        (MINIBUS, 'Minibus'),
        (OTHER, 'Other'),
        (DEFAULT, '---------')

    ]

    type = models.CharField(
        blank=False,
        null=False,
        max_length=CAR_TYPE_MAX_LEN,
        choices=CAR_TYPES,
        default=DEFAULT,
        verbose_name='Type'
    )

    model = models.CharField(
        blank=False,
        null=False,
        max_length=MODEL_MAX_LEN,
        validators=[MinLengthValidator(
            MODEL_MIN_LEN,
            f'Model name should be at least {MODEL_MIN_LEN} long.')
        ],
        verbose_name='Model'
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(YEAR_MANUFACTURED_MIN_VAL,
                              YEAR_MANUFACTURED_ERR_MSG),
            MaxValueValidator(YEAR_MANUFACTURED_MAX_VAL,
                              YEAR_MANUFACTURED_ERR_MSG),
        ],
        verbose_name='Year'
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL'
    )

    price = models.DecimalField(
        blank=False,
        null=False,
        max_digits=200,
        decimal_places=3,
        validators=[MinValueValidator(1), ],
        verbose_name='Price'
    )
