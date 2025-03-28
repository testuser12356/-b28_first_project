from django.contrib import messages
from django.shortcuts import render, redirect

import main.forms as forms
import main.models as models


def list_category(request):
    objects_list = models.Category.objects.all()
    return render(request,
                  "list_category.html",
                  context={"objects_list": objects_list})


def create_category(request):
    if request.POST:
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Yangi category qo'shildi")
            return redirect("/")
    form = forms.CategoryForm()
    return render(request, "crud_form.html", {"form": form})
