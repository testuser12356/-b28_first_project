from django import forms

import main.models as models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = "__all__"


class NewsForm(forms.ModelForm):
    class Meta:
        model = models.News
        fields = ("category", "image", "title", "subtitle", "post")
