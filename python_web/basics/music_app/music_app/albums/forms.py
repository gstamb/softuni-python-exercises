from django import forms
from music_app.albums.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['users',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image_url"].widget.attrs.update({
            "placeholder": "Image URL",
            "title": "Image URL",
        })
        self.fields["image_url"].label = "Image URL"

        self.fields["artist"].widget.attrs.update({
            "placeholder": "Artist Name",
            "title": "Artist Name",
        })
        self.fields["artist"].label = "Artist Name"

        self.fields["album_name"].widget.attrs.update({
            "placeholder": "Album Name",
            "title": "Album Name",
        })
        self.fields["album_name"].label = "Album Name"

        self.fields["description"].widget.attrs.update({
            "placeholder": "Description",
            "title": "Description",
        })

        self.fields["price"].widget.attrs.update({
            "placeholder": "Price",
            "title": "Price",
        })


class AlbumDeleteForm(AlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.disabled = True
