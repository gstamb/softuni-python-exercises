from django.contrib import admin

from templates_advanced.todos.models import Todo

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
