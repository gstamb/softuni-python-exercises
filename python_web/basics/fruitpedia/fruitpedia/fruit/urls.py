from django.urls import path
from fruitpedia.fruit.views import index,dashboard, fruit_details, add_fruit, delete_fruit, edit_fruit


urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('details:<int:pk>', fruit_details, name='fruit details'),
    path('create/', add_fruit, name='add fruit'),
    path('delete/<int:pk>', delete_fruit, name='delete fruit'),
    path('edit/<int:pk>', edit_fruit, name='edit fruit'),

]