from django.contrib import admin

from app.models import Expense, Profile

admin.site.register(Profile)
admin.site.register(Expense)
