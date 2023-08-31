from django import forms
from carcollection.car_app.models.car_model import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarEditForm(CarCreateForm):
    pass


class CarDeleteForm(CarCreateForm):
    def __init__(self, *args, **kwargs):
        super(CarCreateForm, self).__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.disabled = True
