from django.urls import path
from plantapp.user_profile.views import create_profile, show_profile, edit_profile, delete_profile


urlpatterns = [
    path('create/', create_profile, name='create-profile'),
    path('details/', show_profile, name='show-profile'),
    path('edit/', edit_profile, name='edit-profile'),
    path('delete/', delete_profile, name='delete-profile'),

]
