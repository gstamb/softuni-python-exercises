from django.urls import path
from fruitpedia.user_profile.views import create_profile, profile_details,edit_profile, delete_profile


urlpatterns = [
    path('create/', create_profile, name='create profile'),
    path('details/', profile_details, name='details profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/<int:pk>', delete_profile, name='delete profile'),
]
