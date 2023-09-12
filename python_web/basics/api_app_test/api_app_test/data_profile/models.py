from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from api_app_test.user_auth.models import CustomUser


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/users/id/<filename>
    return 'users/{0}/{1}'.format(instance.id, filename)


def customer_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/customer/id/<filename>
    return 'customers/{0}/{1}'.format(instance.id, filename)


class UserProfile(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    country = CountryField(blank_label="(select country)", blank=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image_url = models.ImageField(
        upload_to=user_directory_path, default='static/None/default_entity_image.webp')


class CustomerProfile(models.Model):
    company_identifier = models.CharField(max_length=40, blank=True)
    business_name = models.CharField(max_length=40, blank=True)
    country = CountryField(blank_label="(select country)", blank=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image_url = models.ImageField(
        upload_to=customer_directory_path,  default='static/None/default_entity_image.webp')
