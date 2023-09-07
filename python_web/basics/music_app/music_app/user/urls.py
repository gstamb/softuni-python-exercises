from django.urls import path

from music_app.user.views import user_home,show_profile,delete_profile


urlpatterns = [
    path('', user_home, name='user home'),
    path('profile/', show_profile, name='show profile'),
    path('delete/', delete_profile, name='delete profile'),
]