from api_app_test.data_profile.models import CustomerProfile, UserProfile
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
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


@receiver(post_save, sender=UserProfile)
def complete_profile_receiver(sender, instance, **kwargs):
    excluded_fields = ( 'id', 'image_url')

    fields = [f.name for f in instance._meta.get_fields()
              if f.name not in excluded_fields]
    user_can_post_group = Group.objects.get(name='user_add_delete_trip') 
    user_allowed_to_post = all(bool(getattr(instance, field)) for field in fields)
    if user_allowed_to_post:
        user_can_post_group.user_set.add(instance.email)
    else:
        user_can_post_group.user_set.remove(instance.email)