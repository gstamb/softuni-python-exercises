from django import forms

from plantapp.plant.models import PlantModel


class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'


class PlantEditForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'


class PlantDeleteForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.disabled = True
