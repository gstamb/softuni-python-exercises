from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from games_play_app.play_app.forms import DeleteGameForm

from games_play_app.play_app.models.game_model import Game
from django.views.generic.edit import FormMixin, ModelFormMixin


class GameCreateView(CreateView):
    model = Game
    fields = '__all__'
    template_name = 'create-game.html'
    success_url = reverse_lazy('dashboard')


class GameDetailView(DetailView):
    model = Game
    template_name = 'details-game.html'
    context_object_name = 'game'


class GameEditView(UpdateView):
    model = Game
    fields = '__all__'
    template_name = 'edit-game.html'
    success_url = reverse_lazy('dashboard')

 

class GameDeleteView(DeleteView):
    model = Game
    template_name = 'delete-game.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, *args, **kwargs):
        context = super(GameDeleteView, self).get_context_data(
            *args, **kwargs)
        
        instance = self.get_object()
        
        context['form'] = DeleteGameForm(instance=instance) 
        
        return context
    

    