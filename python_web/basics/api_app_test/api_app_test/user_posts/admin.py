from django.contrib import admin
from .models import Trip, TripImage


class TripImageInline(admin.TabularInline):
    model = TripImage


class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city', 'author', 'date_created')
    list_filter = ('country', 'city', 'author')
    search_fields = ('title', 'destination', 'author__username')
    inlines = [TripImageInline]


admin.site.register(Trip, TripAdmin)
