from django.core.validators import MinLengthValidator
from django.db import models
from plantapp.core.custom_validator import contains_only_letters

# Create your models here.
INDOOR_PLANTS = 'Indoor Plants'
OUTDOOR_PLANTS = "Outdoor Plants"
DEFAULT = 'Unknown'

PLANT_OPTIONS = (
    (OUTDOOR_PLANTS, "Outdoor Plants"),
    (INDOOR_PLANTS, "Indoor Plants"),
    (DEFAULT, '---------')
)

MAX_LEN_PT = 14
MAX_LEN_PN = 20

MAX_DIGITS = 50
DECIMAL_PLACES = 2


class PlantModel(models.Model):
    plant_type = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_PT,
        choices=PLANT_OPTIONS,
        default=DEFAULT,
        verbose_name='Type'
    )

    plant_name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_PN,
        validators=[MinLengthValidator(2), contains_only_letters],
        verbose_name='Name'
        
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL'
        
    )

    description = models.TextField(
        blank=False,
        null=False,
        verbose_name='Description'

    )

    price = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        blank=False,
        null=False,
        verbose_name='Price'
        
    )
