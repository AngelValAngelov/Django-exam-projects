from django import forms

from myMusicApp.web.models import Album, Profile


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'name': 'Album Name',
            'image': 'Image URL',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                },
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                },
            ),
            'genre': forms.Select(
                choices=Album.GENRES,
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description',
                },
            ),
            'image': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL',
                },
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                },
            ),
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'name': 'Album Name',
            'image': 'Image URL',
        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'name': 'Album Name',
            'image': 'Image URL',
        }


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'



