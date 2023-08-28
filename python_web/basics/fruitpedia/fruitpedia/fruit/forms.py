from django import forms

from fruitpedia.fruit.models import FruitModel


class FruitCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30,
        min_length=2,
        required=True,
        widget=forms.TextInput(
            attrs={'type': 'text', 'name': 'name', 'id': 'name-name', 'placeholder': 'Fruit Name'}
        ),

    )
    image_url = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'type': 'text', 'name': 'imageUrl', 'id': 'Fruit-image', 'placeholder': 'Fruit Image URL'}
        ),
    )

    description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'name': 'description', 'id': 'fruit-description', 'placeholder': 'Fruit Description', 'rows': '10',
                   'cols': '50'}
        ),
    )

    nutrition = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'name': 'nutrition', 'id': 'fruit-nutrition', 'placeholder': 'Nutrition Info', 'rows': '10',
                   'cols': '50'}
        ),
    )
    
    def clean(self):
        cleaned_data = super().clean()
        fruit_name = cleaned_data.get("name")
        msg = 'Fruit name should contain only letters!'
 
        if not all([x.isalpha() for x in fruit_name]):
            self._errors['fruit_ name'] = self.error_class([
                msg])

        return self.cleaned_data
    class Meta:
        model = FruitModel
        fields = '__all__'
