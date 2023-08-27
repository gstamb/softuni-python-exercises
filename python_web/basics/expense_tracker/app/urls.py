from django.urls import path
from app.views.profiles import create_profile, edit_profile, delete_profile, profile_page, index
from app.views.expenses import create_expense, edit_expense, delete_expense

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_expense, name='create expense'),
    path('delete/<int:pk>', delete_expense, name='delete expense'),
    path('edit/<int:pk>', edit_expense, name='edit expense'),
    path('profile/', profile_page, name='profile'),
    path('profile/create', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
]
