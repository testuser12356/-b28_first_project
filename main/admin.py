from django.contrib import admin

import main.models as models


# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_editable = ("order_num",)
    list_display_links = ("id", "name")
    list_display = ("id", "name", "order_num")


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_editable = ("category",)
    search_fields = ("id", "title")
    readonly_fields = ("views_count",)
    list_display_links = ("id", "title")
    list_filter = ("category", "published_at")
    list_display = (
        "id", "title", "category",
        "published_at", "views_count"
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "message", "news", "added_at")
    list_display_links = ("id", "message")
