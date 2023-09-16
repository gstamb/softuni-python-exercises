from api_app_test.data_profile.models import CustomerProfile, UserProfile
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver

from api_app_test.user_posts.models import Trip


@receiver(pre_delete, sender=CustomerProfile)
def remote_related(sender, instance, **kwargs):
    pass


@receiver(pre_delete, sender=UserProfile)
def remote_related_trips(sender, instance, **kwargs):
    owner_id = instance.email.id
    trips = Trip.objects.filter(author=owner_id).all()
    for trip in trips:
        for image in trip.photo.all():
            image.photo.delete(save=True)
            image.thumbnail.delete(save=True)
