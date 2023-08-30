from django.urls import path
from plantapp.plant.views import show_homepage, show_catalogue, create_plant, show_details, edit_plant, delete_plant

urlpatterns = [
    path('', show_homepage, name='show-index'),
    path('catalogue/', show_catalogue, name='show-catalogue'),
    path('create/', create_plant, name='create-plant'),
    path('details/<int:pk>', show_details, name='show-details'),
    path('edit/<int:pk>', edit_plant, name='edit-plant'),
    path('delete/<int:pk>', delete_plant, name='delete-plant'),
]
