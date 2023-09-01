from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from games_play_app.play_app.models.profile_model import Profile
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
