from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import constraints
POP = "Pop Music"
JAZZ = "Jazz Music"
RNB = "R&B Music"
ROCK = "Rock Music"
COUNTRY = "Country Music"
DANCE = "Dance Music"
HIPHOP = "Hip Hop Music"
OTHER = "Other"
DEFAULT = "---------"

CHOICES_MUSIC = (
    (POP, "Pop Music"),
    (JAZZ, "Jazz Music"),
    (RNB, "R&B Music"),
    (ROCK, "Rock Music"),
    (COUNTRY, "Country Music"),
    (DANCE, "Dance Music"),
    (HIPHOP, "Hip Hop Music"),
    (OTHER, "Other"),
    (DEFAULT, "---------")
)


class Album(models.Model):
    album_name = models.CharField(
        blank=False,
        max_length=30,
    )

    artist = models.CharField(
        blank=False,
        max_length=30,
    )

    genre = models.CharField(
        blank=False,
        choices=CHOICES_MUSIC,
        default=DEFAULT,
        max_length=30
    )

    description = models.TextField(
        blank=True
    )

    image_url = models.URLField(
        blank=False
    )

    price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[
            MinValueValidator(0)],
    )

    users  = models.ManyToManyField(User)
    

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['album_name', 'artist'], name='unique_album'),
        ]