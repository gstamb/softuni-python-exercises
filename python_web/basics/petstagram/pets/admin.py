from django.contrib import admin

from pets.models import Pet, Like

class LikeInlineAdmin(admin.TabularInline):
    model = Like
class PetAdmin(admin.ModelAdmin):
    list_display = ('type', 'name')
    list_filter = ('type',)
    inlines = [
        LikeInlineAdmin
    ]

admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
