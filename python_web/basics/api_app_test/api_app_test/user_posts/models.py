from decimal import Decimal
from tokenize import triple_quoted
from django.db import models
from django.db import models
from django.dispatch import receiver
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from api_app_test.user_auth.models import CustomUser
from django.db.models.signals import post_save


def trip_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/trip/userid/<filename>
    return 'trip/{0}/{1}'.format(instance.trip.author.id, filename)


class Trip(models.Model):
    USER_TRIP_RATING = (
        (Decimal("1.0"), "★☆☆☆☆ (1/5)"),
        (Decimal("2.0"), "★★☆☆☆ (2/5)"),
        (Decimal("3.0"), "★★★☆☆ (3/5)"),
        (Decimal("4.0"), "★★★★☆ (4/5)"),
        (Decimal("5.0"), "★★★★★ (5/5)"),
    )
    title = models.CharField(max_length=255, unique=False)

    country = CountryField(blank_label="(select country)", blank=False)
    city = models.CharField(max_length=50, blank=False)

    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    review = models.TextField(blank=True, max_length=2000)
    rating = models.DecimalField(null=True,
        blank = True,
        max_digits=2, decimal_places=1, choices=USER_TRIP_RATING)


class TripImage(models.Model):
    trip = models.ForeignKey(
        Trip, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(
        upload_to=trip_directory_path,  default='static/None/default_trip_image.webp')
    description = models.TextField(blank=True, max_length=300)


 