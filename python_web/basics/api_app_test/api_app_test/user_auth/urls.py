from django.urls import path
from api_app_test.user_auth.views.common.home import index
from api_app_test.user_auth.views.common.login import UserLogin
from api_app_test.user_auth.views.common.logout import sign_out
from api_app_test.user_auth.views.common.register import EntityRegisterView
 

urlpatterns = [
    path('', index, name='index'),
    path('register/', EntityRegisterView.as_view(), name='register'),
    path('register/customer/', EntityRegisterView.as_view(), name='register customer'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', sign_out, name='loout'),
]
