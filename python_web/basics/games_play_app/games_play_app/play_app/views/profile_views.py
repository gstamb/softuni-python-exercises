from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from games_play_app.play_app.models.profile_model import Profile
from django.db.models import Avg, Count

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = self.get_object()

        annotated_profile = Profile.objects.annotate(
            game_count=Count('game'),
            avg_rating=Avg('game__rating')
        ).filter(pk=profile.pk).first()

        context['count_games'] = annotated_profile.game_count or 0
        context['avg_rating'] = "{:.1f}".format(
            annotated_profile.avg_rating or 0.0)

        return context


class ProfileEditView(UpdateView):
    model = Profile
    fields = '__all__'
    template_name = 'edit-profile.html'

    def get_success_url(self):
        profile_id = self.kwargs['pk']
        return reverse_lazy('details-profile', kwargs={'pk': profile_id})

    def get_form(self, form_class=None):
        form = super(ProfileEditView, self).get_form(form_class)
        form.fields['password'].widget = forms.HiddenInput()
        return form


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'delete-profile.html'
    success_url = reverse_lazy("homepage")
