from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from api_app_test.user_auth.forms import RegisterForm
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group


from api_app_test.user_auth.models import CustomUser


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = RegisterForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "role", 'id']
    list_filter = ["role"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["role"]}),
        ("Permissions", {"fields": []}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email",  "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)

class UserInLine(admin.TabularInline):
    model = Group.user_set.through
    extra = 0


@admin.register(Group)
class GenericGroup(GroupAdmin):
    inlines = [UserInLine]
