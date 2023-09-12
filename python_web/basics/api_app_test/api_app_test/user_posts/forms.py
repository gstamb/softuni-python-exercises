from django import forms
from api_app_test.user_posts.models import Trip, TripImage


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ["title", "country", "city", "review", "rating"]


class TripImageForm(forms.ModelForm):
    class Meta:
        model = TripImage
        fields = ["images"]
