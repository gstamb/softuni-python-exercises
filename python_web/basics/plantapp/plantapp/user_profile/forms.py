from django import forms

from plantapp.user_profile.models import ProfileModel


class BaseCreateFormPlant(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileCreateForm(BaseCreateFormPlant):
    class Meta:
        model = ProfileModel
        fields = ('username', 'first_name', 'last_name')


class ProfileEditForm(BaseCreateFormPlant):
    pass
