from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from api_app_test.user_auth.models import CustomUser


class UserProfile(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    country = CountryField(blank_label="(select country)", blank=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class CustomerProfile(models.Model):
    company_identifier = models.CharField(max_length=40, blank=True)
    business_name = models.CharField(max_length=40, blank=True)
    country = CountryField(blank_label="(select country)", blank=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
