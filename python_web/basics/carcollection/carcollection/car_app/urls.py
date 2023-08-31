from django.urls import path
from carcollection.car_app.views.navigation import index, catalogue
from carcollection.car_app.views.profile_views import create_profile, details_profile, edit_profile, delete_profile
from carcollection.car_app.views.car_views import add_car, details_car, edit_car, delete_car

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),

    path('profile/create/', create_profile, name='create-profile'),
    path('profile/details/', details_profile, name='details-profile'),
    path('profile/edit/', edit_profile, name='edit-profile'),
    path('profile/delete/', delete_profile, name='delete-profile'),

    path('car/create/', add_car, name='add-car'),
    path('car/<int:pk>/details/', details_car, name='details-car'),
    path('car/<int:pk>/edit/', edit_car, name='edit-car'),
    path('car/<int:pk>/delete/', delete_car, name='delete-car'),

]
