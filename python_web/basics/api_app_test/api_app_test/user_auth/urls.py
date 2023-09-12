from django.urls import path
from api_app_test.user_auth.views import EntityRegisterView, UserLogin, logOut, HomePageView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('register/user', EntityRegisterView.as_view(), name='register user'),
    path('register/customer/', EntityRegisterView.as_view(),
         name='register customer'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logOut.as_view(), name='logout'),
]
