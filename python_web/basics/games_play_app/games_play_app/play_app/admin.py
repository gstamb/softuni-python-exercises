from django.contrib import admin
from games_play_app.play_app.models.game_model import Game
from games_play_app.play_app.models.profile_model import Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Game)