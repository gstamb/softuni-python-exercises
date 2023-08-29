from django import forms

from fruitpedia.user_profile.models import UserProfile


class BaseUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        msg = "Your name must start with a letter!"

        if not first_name[0].isalpha():
            self._errors['first_name'] = self.error_class([
                msg])
        if not last_name[0].isalpha():
            self._errors['last_name'] = self.error_class([
                msg])

        return self.cleaned_data


class UserCreateForm(BaseUserForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'text', 'name': 'first_name', 'id': 'first-name', 'placeholder': 'First Name'}
        ),

    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'text', 'name': 'last-name', 'id': 'last-name', 'placeholder': 'Last Name'}
        ),
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'email', 'name': 'register-email', 'id': 'register-email', 'placeholder': 'Email'}
        ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'type': 'password', 'name': 'register-password', 'id': 'register-password',
                   'placeholder': 'Password'}
        ),
    )

    image_url = forms.URLField(
        required=False
    )

    age = forms.IntegerField(
        required=False

    )


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'image_url', 'age')
