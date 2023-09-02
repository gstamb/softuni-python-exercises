
from django import forms

from games_play_app.play_app.models.game_model import Game


class DeleteGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True