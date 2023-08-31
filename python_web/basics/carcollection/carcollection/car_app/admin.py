from django.contrib import admin
from carcollection.car_app.models.user_model import Profile
from carcollection.car_app.models.car_model import Car

# Register your models here.
admin.site.register(Profile)
admin.site.register(Car)
