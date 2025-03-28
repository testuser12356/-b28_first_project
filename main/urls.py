from django.urls import path

import main.views as views

category = [
    path("category/create/", views.create_category)
]

urlpatterns = [
    path("", views.home),
    path("news-detail/<int:news_id>", views.news_detail),
    path("news-list/category/<int:category_id>", views.category_list)
]

urlpatterns += category
