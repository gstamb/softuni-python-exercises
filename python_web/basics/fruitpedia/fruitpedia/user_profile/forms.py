from django import forms


class UserCreateForm(forms.Form):
    first_name = forms.CharField(
        max_length=25,
        min_length=2,
        required=True,
        widget=forms.TextInput(
            attrs={'type': 'text','name':'first_name', 'id':'first-name', 'placeholder': 'First Name'}
        ),

    )
    last_name = forms.CharField(
        max_length=35,
        min_length=1,
        required=True,  
        widget=forms.TextInput(
            attrs={'type': 'text','name':'last-name', 'id':'last-name', 'placeholder': 'Last Name'}
        ),      
    )

    email = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={'type': 'email','name':'register-email', 'id':'register-email', 'placeholder': 'Email'}
        ),  
    )
    
    password = forms.CharField(
        min_length=8,
        max_length=20,
        required=True,
                widget=forms.PasswordInput(
            attrs={'type': 'password','name':'register-password', 'id':'register-password', 'placeholder': 'Password'}
        ),  
    )
    
    image_url = forms.URLField(
        required=False
    )
 

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


class UserEditForm(UserCreateForm):
        password = forms.CharField(
        min_length=8,
        max_length=20,
        required=False,
                widget=forms.TextInput(
            attrs={'type': 'password','name':'register-password', 'id':'register-password', 'placeholder': 'Password'}
        ),  
    )
        