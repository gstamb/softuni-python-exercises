
from django.urls import include, path
from music_app.authentication.views import  register, login_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register user'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', login_user, name='home')
    
]
