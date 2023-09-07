from django.urls import path
from music_app.albums.views import add_album, delete_album, details_album, edit_album, show_albums


urlpatterns =[
    path('add/', add_album, name='add album'),
    path('details/<int:pk>/', details_album, name='details album'),
    path('delete/<int:pk>/', delete_album, name='delete album'),
    path('edit/<int:pk>/', edit_album, name='edit album'),
    path('show/', show_albums , name='show albums')
]