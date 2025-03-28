from django import forms

import main.models as models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = "__all__"
