
from django import forms

from api_app_test.data_profile.models import CustomerProfile, UserProfile


class UserUpdateForm(forms.ModelForm):
    # email = forms.CharField(max_length=255, required=True)

    class Meta:
        model = UserProfile
        exclude = ('email', 'id', 'image_url')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     instance = kwargs.get('instance')
    #     if instance:
    #         self.initial['email'] = instance.email.email


class CustomerUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomerProfile
        exclude = ('email', 'id', 'image_url' )

  
