from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from games_play_app.play_app.models.profile_model import Profile
from games_play_app.play_app.models.game_model import Game

from django import forms


class ProfileCreateView(CreateView):
    model = Profile
    fields = ['email', 'age', 'password']
    template_name = 'create-profile.html'
    success_url = reverse_lazy("homepage")

    def get_form(self, form_class=None):
        form = super(ProfileCreateView, self).get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        return form


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'details-profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailsView, self).get_context_data(
            *args, **kwargs)

        all_games = Game.objects.all()

        games_count = len(all_games)
        rating_sum = sum([x.rating for x in all_games])
        context['count_games'] = games_count
        context['avg_rating'] = "{:.1f}".format(
            0.0 if not games_count else rating_sum / games_count)

        return context


class ProfileEditView(UpdateView):
    model = Profile
    fields = '__all__'
    template_name = 'edit-profile.html'
    success_url = reverse_lazy("homepage")

    def get_form(self, form_class=None):
        form = super(ProfileEditView, self).get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        return form


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'delete-profile.html'
    success_url = reverse_lazy("homepage")
