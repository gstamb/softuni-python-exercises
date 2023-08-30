from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('plantapp.plant.urls')),
    path('profile/', include('plantapp.user_profile.urls'))
]
