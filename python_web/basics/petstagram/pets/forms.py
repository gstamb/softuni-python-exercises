from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from pets.models import Pet


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control rounded-2'}
        )
    )

class EditPetForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'image_url': forms.TextInput(
                attrs={'id': 'img_input'}
            )
        }
    
 