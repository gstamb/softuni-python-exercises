from django.urls import path
from api_app_test.data_profile.views import ProfileDetailsView, ProfileUpdateView, ProfileDeleteView


urlpatterns = [
    path('details/<int:pk>', ProfileDetailsView.as_view(), name='show profile'),
    path('edit/<int:pk>', ProfileUpdateView.as_view(), name='edit profile'),
    path('delete/<int:pk>', ProfileDeleteView.as_view(), name='delete profile'),
]
