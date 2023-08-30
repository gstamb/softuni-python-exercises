from django import forms

from plantapp.user_profile.models import ProfileModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('username', 'first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = "__all__"
