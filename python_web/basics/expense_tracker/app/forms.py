from django import forms
from app.models import Profile, Expense


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "budget"]


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'image_url', 'description', 'price']
