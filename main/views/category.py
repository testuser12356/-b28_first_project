from django.shortcuts import render

import main.forms as forms


def create_category(request):
    form = forms.CategoryForm()
    return render(request, "crud_form.html", {"form": form})
