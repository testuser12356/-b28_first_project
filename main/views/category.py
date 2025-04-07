from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

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
            return redirect("/category/list")
    form = forms.CategoryForm()
    context = {
        "form": form,
        "title": "Category Create"
    }
    return render(request, "crud_form.html", context)


def update_category(request, pk):
    obj = get_object_or_404(models.Category, pk=pk)
    if request.user.is_authenticated:
        if request.POST:
            form = forms.CategoryForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Category Yangilandi")
                return redirect("/category/list")
        form = forms.CategoryForm(instance=obj)
        context = {
            "form": form,
            "title": "Category Update"
        }
        return render(request, "crud_form.html", context)
    else:
        messages.info(request, "Ruxsat yoq")
        return redirect("/")


def delete_category(request, pk):
    obj = get_object_or_404(models.Category, pk=pk)
    if request.user.is_authenticated:
        obj.delete()
        messages.info(request, "Category o'chirildi")
        return redirect("/category/list")
    else:
        messages.info(request, "Ruxsat yoq")
        return redirect("/category/list")
