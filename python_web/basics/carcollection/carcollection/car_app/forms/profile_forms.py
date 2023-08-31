from django import forms
from carcollection.car_app.models.user_model import Profile


class ProfileCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        exclude = ('first_name', 'last_name', 'image_url')


class ProfileEditForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = Profile
        fields = '__all__'
