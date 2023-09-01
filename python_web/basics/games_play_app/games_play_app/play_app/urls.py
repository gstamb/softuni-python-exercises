from django.urls import path
from games_play_app.play_app.views.index_views import HomepageView, DashboardView
from games_play_app.play_app.views.profile_views import ProfileCreateView



urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    path('profile/create/' , ProfileCreateView.as_view(), name='create-profile')
]



