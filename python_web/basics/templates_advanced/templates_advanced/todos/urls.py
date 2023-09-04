from django.urls import path

from templates_advanced.todos.views import index

urlpatterns = [
    path('', index, name='index')
]