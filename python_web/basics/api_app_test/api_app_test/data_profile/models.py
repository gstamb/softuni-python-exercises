from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from api_app_test.user_auth.models import CustomUser


def file_dir_path(instance, filename):
    suffix_index = instance.__class__.__name__.index("P")
    entity = instance.__class__.__name__[:suffix_index].lower()
    return '{0}/{1}/profile_image/{2}'.format(entity, instance.email_id, filename)


class UserProfile(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    country = CountryField(blank_label="(select country)", blank=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='user')
    image_url = models.ImageField(
        upload_to=file_dir_path, blank=True)

    def get_profile_image(self):
        if self.image_url and hasattr(self.image_url, 'url'):
            return self.image_url.url
        return settings.MEDIA_URL + 'static/None/default_entity_image.webp'


class CustomerProfile(models.Model):
    company_identifier = models.CharField(max_length=40, blank=True)
    business_name = models.CharField(max_length=40, blank=True)
    country = CountryField(blank_label="(select country)", blank=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='customer')
    image_url = models.ImageField(
        upload_to=file_dir_path, default='static/None/default_entity_image.webp')

    def get_profile_image(self):
        if self.image_url and hasattr(self.image_url, 'url'):
            return self.image_url.url
        return settings.MEDIA_URL + 'static/None/default_entity_image.webp'
