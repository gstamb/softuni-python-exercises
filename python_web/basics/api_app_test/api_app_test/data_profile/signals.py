from api_app_test.data_profile.models import CustomerProfile, UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from api_app_test.user_auth.models import CustomUser


@receiver(post_save, sender=CustomUser)
def my_handler(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'customer':
            profile = CustomerProfile()
            profile.email = instance
        else:
            profile = UserProfile()
            profile.email = instance
        profile.save()
