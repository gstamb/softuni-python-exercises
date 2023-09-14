from django.urls import path
from api_app_test.user_posts.views import ShowUserTrips, CreateTripView, ShowAllUserTrips, ShowTripDetails

urlpatterns = [
    path('', CreateTripView.as_view(), name='add trip'),
    path('trips/', ShowUserTrips.as_view(), name='user trips'),
    path('community-trips/', ShowAllUserTrips.as_view(), name='community trips'),
    path('details/<slug:slug>', ShowTripDetails.as_view(), name='details trip'),
    
]
