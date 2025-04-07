from django.urls import path

import main.views as views

news = [
    path("news/list", views.news_list),
    path("news/create/", views.news_create),
    path("news/update/<int:pk>/", views.news_update),
    path("news/delete/<int:pk>/", views.news_delete),
]

category = [
    path("category/list", views.list_category),
    path("category/create/", views.create_category),
    path("category/update/<int:pk>/", views.update_category),
    path("category/delete/<int:pk>/", views.delete_category),
]

urlpatterns = [
    path("", views.home),
    path("news-detail/<int:news_id>", views.news_detail),
    path("news-list/category/<int:category_id>", views.category_list)
]

urlpatterns += category + news
