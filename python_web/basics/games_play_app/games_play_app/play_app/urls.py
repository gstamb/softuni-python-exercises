from django.urls import path
from games_play_app.play_app.views.index_views import HomepageView, DashboardView
from games_play_app.play_app.views.profile_views import ProfileCreateView, ProfileDetailsView, ProfileEditView , ProfileDeleteView
from games_play_app.play_app.views.game_views import GameCreateView, GameDetailView, GameEditView, GameDeleteView


urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('profile/create/', ProfileCreateView.as_view(), name='create-profile'),
    path('profile/details/<int:pk>', ProfileDetailsView.as_view(), name='details-profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='edit-profile'),
    path('profile/delete/<int:pk>', ProfileDeleteView.as_view(), name='delete-profile'),


    path('create/', GameCreateView.as_view(), name='create-game'),
    path('details/<int:pk>', GameDetailView.as_view(), name='details-game'),
    path('edit/<int:pk>', GameEditView.as_view(), name='edit-game'),
    path('delete/<int:pk>', GameDeleteView.as_view(), name='delete-game'),
]
