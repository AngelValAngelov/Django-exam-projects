from django import forms

from myPlantApp.web.models import Profile, Plant


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('picture',)


class CreatePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class EditPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class DeletePlantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Plant
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Plant.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
