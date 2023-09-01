from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from games_play_app.play_app.models.game_model import Game


class HomepageView(TemplateView):
    template_name = "home-page.html"


class DashboardView(ListView):
    model = Game
    context_object_name = 'games'
    template_name = "dashboard.html"
