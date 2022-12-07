from django import forms

from recipes.web.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class DeleteRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeleteRecipeForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = '__all__'

