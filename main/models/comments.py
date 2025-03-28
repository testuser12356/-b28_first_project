from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    news = models.ForeignKey(
        "News", on_delete=models.CASCADE,
        related_name="comments")
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name="my_comments")
    message = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user}"

    class Meta:
        db_table = "comments"
        ordering = ("-added_at",)
