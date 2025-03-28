from django import forms

import main.models as models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ("message", )
