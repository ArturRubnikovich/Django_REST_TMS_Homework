from django import forms
from ckeditor.fields import CKEditorWidget

from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ["name", "preview_image", "time_minutes", "category", "ingredients", "description"]
        widgets = {
            "description": CKEditorWidget()
        }


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ["name", "calories", "description"]
        widgets = {
            "name": forms.TextInput(),
            "calories": forms.NumberInput(),
            "description": CKEditorWidget()
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and Ingredient.objects.filter(name=name).exists():
            raise forms.ValidationError('Ингредиент с таким названием уже существует')
        return name
