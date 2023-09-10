from api_app_test.user_auth.forms.base.create import RegisterForm


class CustomerRegisterForm(RegisterForm):
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.role = 'customer'
        if commit:
            user.save()
        return user
