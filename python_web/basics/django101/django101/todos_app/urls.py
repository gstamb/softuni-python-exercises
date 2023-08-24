from django.urls import path
from django101.todos_app.views import index, create_todo, edit_todo, delete_todo, mark_todo_done

urlpatterns = [
    path('', index, name='todos_app index'),
    path('create/', create_todo, name='create-todo'),
    path('edit/<int:pk>', edit_todo, name='edit todo'),
    path('delete/<int:pk>', delete_todo, name='delete todo'),
    path('mark-done/<int:pk>', mark_todo_done, name='mark todo done'),
]
