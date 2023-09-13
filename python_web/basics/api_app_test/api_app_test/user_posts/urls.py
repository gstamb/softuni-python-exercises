from django.urls import path
from api_app_test.user_posts.views import ShowUserTrips, CreateTripView, ShowAllUserTrips

urlpatterns = [
    path('', CreateTripView.as_view(), name='add trip'),
    path('mytrips/', ShowUserTrips.as_view(), name='user trips'),
    path('community-trips/', ShowAllUserTrips.as_view(), name='community trips')
]
