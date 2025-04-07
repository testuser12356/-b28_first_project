from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

import main.forms as forms
import main.models as models


def news_create(request):
    if request.POST:
        form = forms.NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Yangilik saqlandi")
            return redirect("/news/list")
        else:
            messages.error(request, f"{form.errors}")
    form = forms.NewsForm()
    context = {
        "form": form,
        "title": "News Create"
    }
    return render(request, "crud_form.html", context)


def news_list(request):
    objects_list = models.News.objects.all()
    return render(request, "news_list.html",
                  context={"objects_list": objects_list})


def news_update(request, pk):
    obj = get_object_or_404(models.News, pk=pk)
    if request.POST:
        form = forms.NewsForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Yangilandi")
            return redirect("/news/list")
    form = forms.NewsForm(instance=obj)
    context = {
        "form": form,
        "title": "News Update"
    }
    return render(request, "crud_form.html", context)


def news_delete(request, pk):
    obj = get_object_or_404(models.News, pk=pk)
    if request.user.is_authenticated:
        obj.delete()
        messages.info(request, "Yangilik o'chirilib yuborildi")
        return redirect("/news/list")
    return redirect("/")
