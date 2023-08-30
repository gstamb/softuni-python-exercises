from django import forms

from plantapp.plant.models import PlantModel


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.disabled = True