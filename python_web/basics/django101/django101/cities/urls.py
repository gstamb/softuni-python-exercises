from django.urls import path
from django101.cities import views

urlpatterns = [
    path('', views.index, name='citites index'),
    path('phones/', views.list_phones),
    path('create/', views.create_person)
]
