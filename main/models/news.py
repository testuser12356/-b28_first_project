from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    order_num = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order_num",)


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="news/%Y-%m-%d/")
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=500)
    post = models.TextField()
    published_at = models.DateTimeField()
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-published_at",)
