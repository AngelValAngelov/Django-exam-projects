import os

from django import forms

from expenses_tracker.web.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-file',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-file',
                }
            ),
            'budget': forms.NumberInput(
                attrs={
                    'class': 'form-file',
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-file',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-file',
                }
            ),
            'budget': forms.NumberInput(
                attrs={
                    'class': 'form-file',
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.image.path
        self.instance.delete()
        Expense.objects.all().delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeleteExpenseForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
