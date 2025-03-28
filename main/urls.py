from django.urls import path

import main.views as views

urlpatterns = [
    path("", views.home),
    path("news-list/category/<int:category_id>", views.category_list),
    path("news-detail/<int:news_id>", views.news_detail),
]
