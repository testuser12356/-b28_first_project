from django.shortcuts import render, get_object_or_404, redirect

import main.forms as forms
import main.models as models


# Create your views here.

def home(request):
    object_list = models.News.objects.all()

    if "search" in request.GET:
        search = request.GET.get("search")
        object_list = object_list.filter(title__icontains=search)

    context = {
        "objects_list": object_list
    }
    return render(
        request,
        "home.html",
        context
    )


def category_list(request, category_id):
    object_list = models.News.objects.filter(category_id=category_id)
    context = {
        "objects_list": object_list
    }
    return render(request, "category.html", context)


def news_detail(request, news_id):
    obj = get_object_or_404(models.News, pk=news_id)
    obj.views_count += 1
    obj.save()

    if request.user.is_authenticated:
        if request.POST:
            form = forms.CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.news = obj
                comment.user = request.user
                comment.save()
                return redirect(f"/news-detail/{news_id}")

    form = forms.CommentForm()
    context = {
        "object": obj,
        "form": form
    }

    return render(request, "news_detail.html", context)
