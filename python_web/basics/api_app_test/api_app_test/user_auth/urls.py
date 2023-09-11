from django.urls import path

from api_app_test.user_auth.views import EntityRegisterView, UserLogin, logout, HomePageView



urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('register/user', EntityRegisterView.as_view(), name='register user'),
    path('register/customer/', EntityRegisterView.as_view(), name='register customer'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logout, name='logout'),
]
