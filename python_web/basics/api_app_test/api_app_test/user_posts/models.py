from django.utils import timezone
from decimal import Decimal
from uuid import uuid4
from django.db import models
from django.urls import reverse, reverse_lazy
from django_countries.fields import CountryField
from api_app_test.user_auth.models import CustomUser
from django.conf import settings
from django.utils.text import slugify


def trip_directory_path(instance, filename, is_thumbnail=False):
    base_path = f'{instance.trip.author.role}/{instance.trip.author.id}'
    if is_thumbnail:
        return f'{base_path}/thumbnails/{instance.trip_id}/{filename}'
    else:
        return f'{base_path}/trip_images/{instance.trip_id}/{filename}'


class Trip(models.Model):
    USER_TRIP_RATING = (
        (Decimal("1.0"), "★☆☆☆☆ (1/5)"),
        (Decimal("2.0"), "★★☆☆☆ (2/5)"),
        (Decimal("3.0"), "★★★☆☆ (3/5)"),
        (Decimal("4.0"), "★★★★☆ (4/5)"),
        (Decimal("5.0"), "★★★★★ (5/5)"),
    )
    title = models.CharField(max_length=255, unique=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review = models.TextField(blank=True, max_length=2000)
    rating = models.DecimalField(null=True,
                                 blank=True,
                                 max_digits=2,
                                 decimal_places=1,
                                 choices=USER_TRIP_RATING)

    country = CountryField(blank_label="(select country)", blank=False)
    city = models.CharField(max_length=50, blank=False)

    # utility
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.author, self.country, self.title[:10])

    def get_absolute_url(self):
        return reverse_lazy('trips', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{}-{}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Trip, self).save(*args, **kwargs)


class TripImage(models.Model):
    trip = models.ForeignKey(
        Trip, on_delete=models.CASCADE, related_name='photo')
    photo = models.ImageField(upload_to=trip_directory_path)
    thumbnail = models.ImageField(
        upload_to=lambda instance, filename: trip_directory_path(instance, filename, is_thumbnail=True))
    description = models.TextField(blank=True, max_length=300)
    # utility
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}{}'.format(self.trip.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{}-{}'.format(
                self.trip.title, self.uniqueId))

        self.slug = slugify('{}-{}'.format(self.trip.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(TripImage, self).save(*args, **kwargs)

    def image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        return settings.MEDIA_URL + 'static/None/default_trip_image.webp'
