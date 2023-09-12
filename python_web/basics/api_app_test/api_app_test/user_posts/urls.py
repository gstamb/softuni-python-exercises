from django.urls import path
from api_app_test.user_posts.views import add_trip
 
urlpatterns = [
    path('', add_trip, name='add trip')
]
